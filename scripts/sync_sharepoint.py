#!/usr/bin/env python3
"""
Sync ENS documents from git to SharePoint and embed them in Confluence.

Requires environment variables:
  AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET
  SHAREPOINT_SITE_URL  (e.g. optimimaiimprovements.sharepoint.com:/sites/ENS)
  CONFLUENCE_BASE_URL, CONFLUENCE_USER, CONFLUENCE_API_TOKEN

Usage:
  python scripts/sync_sharepoint.py                   # sync all changed files (git diff)
  python scripts/sync_sharepoint.py --all             # sync ALL mapped files
  python scripts/sync_sharepoint.py --file "path"     # sync one specific file
"""

import argparse
import json
import os
import re
import subprocess
import sys
import unicodedata
import urllib.parse
from pathlib import Path

import requests

# ── Config ──────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFLUENCE_MAP = REPO_ROOT / "confluence_map.md"
SHAREPOINT_FOLDER = "2026"  # root folder in the document library


def strip_accents(s: str) -> str:
    """Remove diacritics/accents from a string for comparison."""
    return "".join(
        c for c in unicodedata.normalize("NFD", s)
        if unicodedata.category(c) != "Mn"
    )

AZURE_TENANT_ID = os.environ.get("AZURE_TENANT_ID", "")
AZURE_CLIENT_ID = os.environ.get("AZURE_CLIENT_ID", "")
AZURE_CLIENT_SECRET = os.environ.get("AZURE_CLIENT_SECRET", "")

CONFLUENCE_BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "https://optimtech-team-a36pyv7e.atlassian.net/wiki")
CONFLUENCE_USER = os.environ.get("CONFLUENCE_USER", "")
CONFLUENCE_API_TOKEN = os.environ.get("CONFLUENCE_API_TOKEN", "")

SHAREPOINT_HOST = "optimimaiimprovements.sharepoint.com"
SHAREPOINT_SITE_PATH = "/sites/ENS"

# Document extensions we sync
SYNC_EXTENSIONS = {".docx", ".xlsx", ".pdf", ".pptx"}


# ── Microsoft Graph Auth ────────────────────────────────────────────────────

def get_graph_token() -> str:
    url = f"https://login.microsoftonline.com/{AZURE_TENANT_ID}/oauth2/v2.0/token"
    data = {
        "client_id": AZURE_CLIENT_ID,
        "client_secret": AZURE_CLIENT_SECRET,
        "scope": "https://graph.microsoft.com/.default",
        "grant_type": "client_credentials",
    }
    resp = requests.post(url, data=data, timeout=30)
    resp.raise_for_status()
    return resp.json()["access_token"]


def graph_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


# ── SharePoint Operations ──────────────────────────────────────────────────

def get_site_id(token: str) -> str:
    url = f"https://graph.microsoft.com/v1.0/sites/{SHAREPOINT_HOST}:{SHAREPOINT_SITE_PATH}"
    resp = requests.get(url, headers=graph_headers(token), timeout=30)
    resp.raise_for_status()
    return resp.json()["id"]


def get_drive_id(token: str, site_id: str) -> str:
    """Get the default document library drive ID."""
    url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive"
    resp = requests.get(url, headers=graph_headers(token), timeout=30)
    resp.raise_for_status()
    return resp.json()["id"]


def upload_file(token: str, drive_id: str, local_path: Path, remote_folder: str) -> dict:
    """Upload a file to SharePoint. Returns the drive item metadata."""
    file_name = local_path.name
    # For files < 4MB use simple upload; larger files need upload session
    file_size = local_path.stat().st_size
    remote_path = f"{remote_folder}/{file_name}"
    encoded_path = urllib.parse.quote(remote_path)

    if file_size < 4 * 1024 * 1024:
        url = f"https://graph.microsoft.com/v1.0/drives/{drive_id}/root:/{encoded_path}:/content"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/octet-stream",
        }
        with open(local_path, "rb") as f:
            resp = requests.put(url, headers=headers, data=f, timeout=120)
        resp.raise_for_status()
        return resp.json()
    else:
        # Create upload session for large files
        url = f"https://graph.microsoft.com/v1.0/drives/{drive_id}/root:/{encoded_path}:/createUploadSession"
        body = {"item": {"@microsoft.graph.conflictBehavior": "replace"}}
        resp = requests.post(url, headers=graph_headers(token), json=body, timeout=30)
        resp.raise_for_status()
        upload_url = resp.json()["uploadUrl"]

        chunk_size = 10 * 1024 * 1024  # 10MB chunks
        with open(local_path, "rb") as f:
            offset = 0
            while offset < file_size:
                chunk = f.read(chunk_size)
                end = offset + len(chunk) - 1
                headers = {
                    "Content-Length": str(len(chunk)),
                    "Content-Range": f"bytes {offset}-{end}/{file_size}",
                }
                resp = requests.put(upload_url, headers=headers, data=chunk, timeout=120)
                resp.raise_for_status()
                offset += len(chunk)
            return resp.json()


def get_embed_url(token: str, drive_id: str, item_id: str) -> str:
    """Get the web URL for the uploaded file, trying multiple approaches."""
    # Approach 1: Try createLink with "view" type (more widely supported)
    url = f"https://graph.microsoft.com/v1.0/drives/{drive_id}/items/{item_id}/createLink"
    for link_type, scope in [("embed", "organization"), ("view", "organization"), ("view", "anonymous")]:
        body = {"type": link_type, "scope": scope}
        resp = requests.post(url, headers=graph_headers(token), json=body, timeout=30)
        if resp.ok:
            return resp.json()["link"]["webUrl"]

    # Approach 2: Fall back to the item's webUrl (always available)
    url = f"https://graph.microsoft.com/v1.0/drives/{drive_id}/items/{item_id}"
    resp = requests.get(url, headers=graph_headers(token), timeout=30)
    resp.raise_for_status()
    return resp.json()["webUrl"]


# ── Confluence Map Parsing ──────────────────────────────────────────────────

def parse_confluence_map() -> dict:
    """Parse confluence_map.md and return {normalized_path: {page_id, title, map_path}} for ALL entries.

    Keys are accent-stripped lowercase paths so real filenames (with accents) match map entries (without).
    Includes both git->confluence and confluence->git entries.
    """
    mapping = {}
    content = CONFLUENCE_MAP.read_text(encoding="utf-8")
    # Match ALL table rows with local path, title, page ID (any sync direction)
    pattern = re.compile(
        r"\|\s*`([^`]+)`\s*\|\s*(.+?)\s*\|\s*(\d+)\s*\|\s*(\w+)\s*\|\s*(?:git\s*->\s*confluence|confluence\s*->\s*git)\s*\|"
    )
    for m in pattern.finditer(content):
        local_path = m.group(1)
        title = m.group(2).strip()
        page_id = m.group(3)
        norm_key = strip_accents(local_path).lower().rstrip("/")
        mapping[norm_key] = {"page_id": page_id, "title": title, "map_path": local_path}
    return mapping


def find_confluence_mapping(confluence_map: dict, file_path: str) -> dict | None:
    """Look up a file path in the confluence map, accent-insensitive.

    Tries exact match first, then walks up parent directories to match
    folder-level entries (e.g. 06_EVIDENCIAS/personal/ for files inside).
    """
    norm = strip_accents(file_path).lower()
    # Try exact file match
    if norm in confluence_map:
        return confluence_map[norm]
    # Try parent directory matches (for folder-level entries like 06_EVIDENCIAS/personal/)
    parts = Path(norm).parts
    for i in range(len(parts) - 1, 0, -1):
        parent = str(Path(*parts[:i])).lower()
        if parent in confluence_map:
            return confluence_map[parent]
    return None


# ── Confluence Update ───────────────────────────────────────────────────────

def get_confluence_page(page_id: str) -> dict:
    url = f"{CONFLUENCE_BASE_URL}/api/v2/pages/{page_id}"
    resp = requests.get(
        url,
        params={"body-format": "storage"},
        auth=(CONFLUENCE_USER, CONFLUENCE_API_TOKEN),
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def update_confluence_with_embed(page_id: str, file_links: list[dict], current_body: str, version_number: int) -> None:
    """Update a Confluence page to include SharePoint document links.

    file_links: list of {"file_name": str, "embed_url": str}
    """
    # Build link list HTML
    links_html = "".join(
        f'<p><a href="{fl["embed_url"]}">{fl["file_name"]} — Abrir en SharePoint</a></p>'
        for fl in file_links
    )

    embed_block = (
        f'<ac:structured-macro ac:name="info">'
        f'<ac:rich-text-body>'
        f'<p><strong>Documentos en SharePoint</strong></p>'
        f'{links_html}'
        f'</ac:rich-text-body>'
        f'</ac:structured-macro>'
    )

    # Remove ALL existing SharePoint info panels (prevents duplicates)
    panel_pattern = re.compile(
        r'<ac:structured-macro[^>]*ac:name="info"[^>]*>.*?Documento[s]? en SharePoint.*?</ac:structured-macro>',
        re.DOTALL,
    )
    cleaned_body = panel_pattern.sub("", current_body).strip()

    # Prepend the single embed block
    new_body = embed_block + "\n" + cleaned_body

    # Get current title
    page_data = get_confluence_page(page_id)
    title = page_data["title"]

    file_names = ", ".join(fl["file_name"] for fl in file_links)

    url = f"{CONFLUENCE_BASE_URL}/api/v2/pages/{page_id}"
    payload = {
        "id": page_id,
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": new_body,
        },
        "version": {
            "number": version_number + 1,
            "message": f"Auto-sync: SharePoint links for {file_names[:80]}",
        },
    }

    resp = requests.put(
        url,
        json=payload,
        auth=(CONFLUENCE_USER, CONFLUENCE_API_TOKEN),
        headers={"Content-Type": "application/json"},
        timeout=30,
    )
    if not resp.ok:
        print(f"  ⚠ Confluence API response: {resp.status_code} - {resp.text[:500]}")
    resp.raise_for_status()
    print(f"  ✓ Confluence page {page_id} updated with {len(file_links)} SharePoint link(s)")


# ── Git Diff ────────────────────────────────────────────────────────────────

def get_changed_files() -> list[str]:
    """Get files changed in the last commit."""
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        # Fallback: list all tracked files
        print("Warning: git diff failed, syncing all files")
        return get_all_syncable_files()
    return [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]


def get_all_syncable_files() -> list[str]:
    """Get all document files that should be synced."""
    files = []
    for ext in SYNC_EXTENSIONS:
        for p in REPO_ROOT.rglob(f"*{ext}"):
            rel = str(p.relative_to(REPO_ROOT))
            # Skip snapshots and temp files
            if rel.startswith("snapshots/") or "~$" in rel:
                continue
            files.append(rel)
    return files


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Sync ENS docs to SharePoint + Confluence")
    parser.add_argument("--all", action="store_true", help="Sync all mapped files")
    parser.add_argument("--file", type=str, help="Sync a specific file path")
    parser.add_argument("--skip-confluence", action="store_true", help="Only upload to SharePoint, skip Confluence update")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be synced without doing it")
    args = parser.parse_args()

    # Validate env vars
    missing = []
    for var in ["AZURE_TENANT_ID", "AZURE_CLIENT_ID", "AZURE_CLIENT_SECRET"]:
        if not os.environ.get(var):
            missing.append(var)
    if not args.skip_confluence:
        for var in ["CONFLUENCE_USER", "CONFLUENCE_API_TOKEN"]:
            if not os.environ.get(var):
                missing.append(var)
    if missing:
        print(f"Error: missing environment variables: {', '.join(missing)}")
        sys.exit(1)

    # Parse confluence map
    confluence_map = parse_confluence_map()
    print(f"Loaded {len(confluence_map)} entries from confluence_map.md")

    # Determine files to sync
    if args.file:
        # Resolve the file path: try exact match first, then fuzzy (accent-insensitive)
        candidate = REPO_ROOT / args.file
        if candidate.exists():
            files_to_sync = [args.file]
        else:
            # Try to find the file by matching without accents
            target_norm = strip_accents(args.file)
            found = None
            for p in REPO_ROOT.rglob("*"):
                if p.is_file() and strip_accents(str(p.relative_to(REPO_ROOT))) == target_norm:
                    found = str(p.relative_to(REPO_ROOT))
                    break
            if found:
                print(f"Resolved '{args.file}' -> '{found}'")
                files_to_sync = [found]
            else:
                files_to_sync = [args.file]  # let it fail with "not found" later
    elif args.all:
        files_to_sync = get_all_syncable_files()
    else:
        files_to_sync = get_changed_files()

    # Filter to syncable extensions
    files_to_sync = [
        f for f in files_to_sync
        if Path(f).suffix.lower() in SYNC_EXTENSIONS
        and not f.startswith("snapshots/")
    ]

    if not files_to_sync:
        print("No document files to sync.")
        return

    print(f"\nFiles to sync: {len(files_to_sync)}")
    for f in files_to_sync:
        print(f"  - {f}")

    if args.dry_run:
        print("\n[DRY RUN] No changes made.")
        return

    # Authenticate with Graph API
    print("\nAuthenticating with Microsoft Graph...")
    token = get_graph_token()
    site_id = get_site_id(token)
    drive_id = get_drive_id(token, site_id)
    print(f"Connected to SharePoint site (drive: {drive_id[:20]}...)")

    # Phase 1: Upload all files to SharePoint and collect embed URLs
    results = {"uploaded": 0, "embedded": 0, "errors": []}
    # Collect links per Confluence page: {page_id: {"links": [...], "mapping": ...}}
    page_links: dict[str, dict] = {}

    for file_path in files_to_sync:
        local_file = REPO_ROOT / file_path
        if not local_file.exists():
            print(f"  ⚠ Skipping {file_path} (file not found)")
            continue

        # Determine SharePoint folder: 2026/<full/subfolder/path>
        parent = str(Path(file_path).parent)
        if parent and parent != ".":
            remote_folder = f"{SHAREPOINT_FOLDER}/{parent}"
        else:
            remote_folder = SHAREPOINT_FOLDER

        try:
            print(f"\n📤 Uploading: {file_path}")
            item = upload_file(token, drive_id, local_file, remote_folder)
            item_id = item["id"]
            results["uploaded"] += 1
            print(f"  ✓ Uploaded to SharePoint: {remote_folder}/{local_file.name}")

            # Get embed URL
            embed_url = get_embed_url(token, drive_id, item_id)
            print(f"  ✓ Embed URL: {embed_url}")

            # Collect for Confluence update
            if not args.skip_confluence:
                mapping = find_confluence_mapping(confluence_map, file_path)
                if mapping:
                    page_id = mapping["page_id"]
                    if page_id not in page_links:
                        page_links[page_id] = {"links": [], "mapping": mapping}
                    page_links[page_id]["links"].append({
                        "file_name": local_file.name,
                        "embed_url": embed_url,
                    })
                else:
                    print(f"  ℹ No Confluence mapping for {file_path}")

        except Exception as e:
            print(f"  ✗ Error uploading {file_path}: {e}")
            results["errors"].append(f"Upload {file_path}: {e}")

    # Phase 2: Batch-update Confluence pages (one update per page, all links at once)
    if not args.skip_confluence and page_links:
        print(f"\n📝 Updating {len(page_links)} Confluence page(s)...")
        for page_id, data in page_links.items():
            try:
                page = get_confluence_page(page_id)
                current_body = page.get("body", {}).get("storage", {}).get("value", "")
                version = page.get("version", {}).get("number", 1)
                update_confluence_with_embed(page_id, data["links"], current_body, version)
                results["embedded"] += 1
            except Exception as e:
                print(f"  ⚠ Confluence update failed for {page_id}: {e}")
                results["errors"].append(f"Confluence {page_id}: {e}")

    # Summary
    print(f"\n{'='*60}")
    print(f"Sync complete: {results['uploaded']} uploaded, {results['embedded']} Confluence pages updated")
    if results["errors"]:
        print(f"Errors ({len(results['errors'])}):")
        for err in results["errors"]:
            print(f"  - {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
