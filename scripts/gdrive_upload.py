"""
Upload a file to a specific Google Drive folder.

Usage:
    python scripts/gdrive_upload.py <file_path> [--folder-name "PMM Portfolio"]

Requires:
    - credentials.json in project root (Google Cloud OAuth client)
    - token.json (run gdrive_auth.py first)
"""

import argparse
import sys
from pathlib import Path

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

ROOT_DIR = Path(__file__).parent.parent
CREDS_FILE = ROOT_DIR / "credentials.json"
TOKEN_FILE = ROOT_DIR / "token.json"
SCOPES = ["https://www.googleapis.com/auth/drive"]

MIMETYPE_MAP = {
    ".md": "text/markdown",
    ".txt": "text/plain",
    ".pdf": "application/pdf",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}


def get_credentials():
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
        if creds.valid:
            return creds
        if creds.expired and creds.refresh_token:
            from google.auth.transport.requests import Request
            creds.refresh(Request())
            with open(TOKEN_FILE, "w") as token:
                token.write(creds.to_json())
            return creds

    if not CREDS_FILE.exists():
        print(f"Error: {CREDS_FILE} not found.")
        print("Run: python scripts/gdrive_auth.py")
        sys.exit(1)

    print("No valid token found. Starting authentication...")
    flow = InstalledAppFlow.from_client_secrets_file(str(CREDS_FILE), SCOPES)
    creds = flow.run_local_server(port=0)
    with open(TOKEN_FILE, "w") as token:
        token.write(creds.to_json())
    return creds


def find_folder(service, folder_name):
    query = (
        f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder' "
        "and trashed = false"
    )
    results = service.files().list(q=query, fields="files(id, name)").execute()
    folders = results.get("files", [])
    if not folders:
        print(f"Error: Folder '{folder_name}' not found in Google Drive.")
        sys.exit(1)
    if len(folders) > 1:
        print(f"Multiple folders named '{folder_name}' found:")
        for f in folders:
            print(f"  - {f['name']} (id: {f['id']})")
        print("Using the first one.")
    return folders[0]["id"]


def upload_file(service, file_path, folder_id, as_doc=False):
    file_name = file_path.name
    ext = file_path.suffix.lower()
    source_mime = MIMETYPE_MAP.get(ext, "application/octet-stream")

    if as_doc:
        doc_name = file_name.rsplit(".", 1)[0]  # strip extension
        file_metadata = {
            "name": doc_name,
            "parents": [folder_id],
            "mimeType": "application/vnd.google-apps.document",
        }
    else:
        doc_name = file_name
        file_metadata = {"name": doc_name, "parents": [folder_id]}

    media = MediaFileUpload(str(file_path), mimetype=source_mime, resumable=True)

    # Check if file already exists in folder
    query = (
        f"name = '{doc_name}' and '{folder_id}' in parents and trashed = false"
    )
    existing = service.files().list(q=query, fields="files(id, name)").execute()
    files = existing.get("files", [])

    if files:
        file_id = files[0]["id"]
        updated = (
            service.files()
            .update(fileId=file_id, media_body=media, fields="id, name, webViewLink")
            .execute()
        )
        print(f"Updated existing file: {updated['name']}")
        print(f"Link: {updated['webViewLink']}")
        return updated

    created = (
        service.files()
        .create(
            body=file_metadata, media_body=media, fields="id, name, webViewLink"
        )
        .execute()
    )
    print(f"Uploaded: {created['name']}")
    print(f"Link: {created['webViewLink']}")
    return created


def main():
    parser = argparse.ArgumentParser(description="Upload file to Google Drive folder")
    parser.add_argument("file_path", type=Path, help="Path to file to upload")
    parser.add_argument(
        "--folder-name",
        default="PMM Portfolio",
        help="Google Drive folder name (default: PMM Portfolio)",
    )
    parser.add_argument(
        "--as-doc",
        action="store_true",
        help="Convert to Google Doc on upload",
    )
    args = parser.parse_args()

    if not args.file_path.exists():
        print(f"Error: File '{args.file_path}' not found.")
        sys.exit(1)

    creds = get_credentials()
    service = build("drive", "v3", credentials=creds)

    print(f"Finding folder '{args.folder_name}'...")
    folder_id = find_folder(service, args.folder_name)

    print(f"Uploading '{args.file_path.name}'...")
    upload_file(service, args.file_path, folder_id, as_doc=args.as_doc)


if __name__ == "__main__":
    main()
