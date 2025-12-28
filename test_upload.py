from utils import extract_folder_id
from drive_service import fetch_images_from_folder
from download_service import download_drive_image
from storage_service import upload_image_to_minio

drive_url = "https://drive.google.com/drive/folders/1MDcjIUDoVLJJprqsKfaUP5uY-rd_jRiz"
folder_id = extract_folder_id(drive_url)

images = fetch_images_from_folder(folder_id)

print("Uploading images to MinIO...")

for img in images:
    data = download_drive_image(img["id"])
    url = upload_image_to_minio(data, img["name"])
    print("Uploaded:", url)
