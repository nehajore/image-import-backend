from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine, SessionLocal
from models import Image

from utils import extract_folder_id
from drive_service import fetch_images_from_folder
from download_service import download_drive_image
from storage_service import upload_image_to_minio

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class ImportRequest(BaseModel):
    folder_url: str


@app.get("/")
def home():
    return {"message": "Hello Neha, your API is running!"}


def background_import_task(folder_url: str):
    folder_id = extract_folder_id(folder_url)

    print("Background task started")
    print(f"Folder ID: {folder_id}")

    images = fetch_images_from_folder(folder_id)

    db = SessionLocal()

    # 🔥 CLEAR PREVIOUS IMAGES (ADD HERE)
    db.query(Image).delete()
    db.commit()

    for img in images:
        print("Processing image:", img["name"])

        file_bytes = download_drive_image(img["id"])
        if not file_bytes:
            continue  # skip private files safely

        storage_url = upload_image_to_minio(file_bytes, img["name"])

        image = Image(
            name=img["name"],
            google_drive_id=img["id"],
            size=img.get("size"),
            mime_type=img.get("mimeType"),
            storage_path=storage_url,
            source="google_drive"
        )

        db.add(image)

    db.commit()
    db.close()

    print("Background task finished")



@app.post("/import/google-drive")
def import_google_drive(
    request: ImportRequest,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        background_import_task,
        request.folder_url
    )

    return {
        "status": "success",
        "message": "Import started in background"
    }
class ImageResponse(BaseModel):
    id: int
    name: str
    google_drive_id: str
    size: str | None
    mime_type: str | None
    storage_path: str
    source: str

    class Config:
        orm_mode = True


@app.get("/images")
def get_images():
    db = SessionLocal()
    images = db.query(Image).all()
    db.close()
    return images

