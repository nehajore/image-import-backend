📂 Google Drive Image Import System

A full-stack web application that imports images from a Google Drive folder, processes them asynchronously, stores them in object storage, and displays them through a web interface.

🚀 Live Demo

Frontend (Netlify):
👉https://incomparable-beignet-ca8698.netlify.app

Backend (Render – Swagger UI):
👉 https://image-import-backend.onrender.com/docs

🧠 Project Overview

This project allows users to:

Paste a Google Drive folder link

Import images asynchronously

Skip restricted/private files safely

Store image metadata in a database

Display imported images in a clean UI

The system is designed with real-world backend practices, including background tasks, error handling, and cloud deployment.

🏗️ Architecture
Frontend (HTML, CSS, JS)
        |
        |  REST API
        |
Backend (FastAPI)
        |
        ├── Google Drive API (image listing & download)
        ├── Database (SQLite – image metadata)
        └── Object Storage (MinIO - local)

🛠️ Tech Stack
Backend

FastAPI

Python

SQLAlchemy

Google Drive API

MinIO (S3-compatible storage)

SQLite

Uvicorn

Frontend

HTML

CSS

JavaScript (Fetch API)

Deployment

Backend: Render

Frontend: Netlify

Version Control: Git & GitHub

📁 Project Structure
image-import-backend/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── drive_service.py
│   ├── download_service.py
│   ├── storage_service.py
│   ├── utils.py
│   ├── requirements.txt
│   └── render.yaml
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── README.md
└── .gitignore

🔗 API Endpoints
Import Images from Google Drive
POST /import/google-drive


Request Body:

{
  "folder_url": "https://drive.google.com/drive/folders/..."
}

Get Imported Images
GET /images


Returns a list of imported images with metadata and storage URLs.

Import Status (Optional)
GET /import/status


Shows real-time import progress.

⚙️ How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/nehajore/image-import-backend.git
cd image-import-backend

2️⃣ Backend Setup
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt


Create .env file:

GOOGLE_DRIVE_API_KEY=your_api_key_here


Run backend:

uvicorn main:app --reload


Swagger UI:

http://127.0.0.1:8000/docs

3️⃣ Frontend Setup
cd frontend


Open index.html in a browser
(or deploy via Netlify)

⚠️ Important Notes & Limitations

Some Google Drive files may be skipped (403 Forbidden) even if publicly viewable.

This is a known limitation when using Google Drive API with API keys.

Private or restricted files are gracefully skipped without breaking the import process.

MinIO is currently local and can be replaced with AWS S3 for production.
