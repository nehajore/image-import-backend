import requests
import os

API_KEY = os.getenv("GOOGLE_DRIVE_API_KEY")

def download_drive_image(file_id: str):
    url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media&key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 403:
        print(f"⚠️ Skipping private file (403): {file_id}")
        return None

    response.raise_for_status()
    return response.content
