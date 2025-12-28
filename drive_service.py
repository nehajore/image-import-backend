import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

API_KEY = os.getenv("GOOGLE_DRIVE_API_KEY")

def get_drive_service():
    return build("drive", "v3", developerKey=API_KEY)

def fetch_images_from_folder(folder_id: str):
    """
    Fetch only image files from a public Google Drive folder
    """
    service = get_drive_service()

    query = f"'{folder_id}' in parents and mimeType contains 'image/'"

    response = service.files().list(
        q=query,
        fields="files(id, name, size, mimeType)"
    ).execute()

    return response.get("files", [])
