from utils import extract_folder_id
from drive_service import fetch_images_from_folder

drive_url = "https://drive.google.com/drive/folders/1MDcjIUDoVLJJprqsKfaUP5uY-rd_jRiz?usp=drive_link"

folder_id = extract_folder_id(drive_url)
print("Folder ID:", folder_id)

images = fetch_images_from_folder(folder_id)

print("Total images found:", len(images))
for img in images:
    print(img)

