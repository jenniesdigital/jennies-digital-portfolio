"""
Google Drive Authentication for JennieAI

Run this once to authenticate with Google Drive.
Opens your browser for sign-in. After authentication, token.json is saved locally.

Usage:
    python scripts/gdrive_auth.py
"""

import sys
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

ROOT_DIR = Path(__file__).parent.parent
CREDS_FILE = ROOT_DIR / "credentials.json"
TOKEN_FILE = ROOT_DIR / "token.json"
SCOPES = ["https://www.googleapis.com/auth/drive"]


def main():
    if not CREDS_FILE.exists():
        print(f"Error: {CREDS_FILE} not found.")
        sys.exit(1)

    print("Opening browser for Google Drive authentication...")
    print("Sign in and grant access.")

    flow = InstalledAppFlow.from_client_secrets_file(str(CREDS_FILE), SCOPES)
    creds = flow.run_local_server(port=0)

    with open(TOKEN_FILE, "w") as token:
        token.write(creds.to_json())

    print(f"Authentication successful! Token saved to {TOKEN_FILE}")


if __name__ == "__main__":
    main()
