let isImporting = false;
const API_BASE = "https://image-import-backend.onrender.com";


function importImages() {
  if (isImporting) return; // 🚫 prevent multiple calls

  const btn = document.getElementById("importBtn");
  const folderUrl = document.getElementById("folderUrl").value.trim();
  const status = document.getElementById("status");

  if (!folderUrl) {
    status.innerText = "❌ Please paste a Google Drive folder link";
    return;
  }

  isImporting = true;
  btn.disabled = true;
  status.innerText = "⏳ Importing images, please wait...";

  fetch(`${API_BASE}/import/google-drive`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ folder_url: folderUrl })
  })
    .then(res => res.json())
    .then(() => {
      status.innerText = "✅ Import finished. Loading images...";
      setTimeout(() => {
        loadImages();
        isImporting = false;
        btn.disabled = false;
      }, 8000);
    })
    .catch(() => {
      status.innerText = "❌ Import failed";
      isImporting = false;
      btn.disabled = false;
    });
}



function loadImages() {
  fetch(`${API_BASE}/images`)
    .then((res) => res.json())
    .then((images) => {
      const container = document.getElementById("imageList");
      container.innerHTML = "";

      if (images.length === 0) {
        container.innerHTML = "<p>No images imported yet.</p>";
        return;
      }

      images.forEach((img) => {
        container.innerHTML += `
          <div class="image-card">
            <img src="${encodeURI(img.storage_path)}" />
            <p>${img.name}</p>
          </div>
        `;
      });
    });
}

