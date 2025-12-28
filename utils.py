from urllib.parse import urlparse

def extract_folder_id(url: str) -> str:
    """
    Extracts Google Drive folder ID from a public folder URL
    """
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split("/")
    return path_parts[-1]
