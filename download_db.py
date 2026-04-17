import gdown
import os

os.makedirs("data", exist_ok=True)

file_path = "data/inventory.db"

if os.path.exists(file_path):
    print("✅ Database already exists. Skipping download.")
else:
    print("⬇️ Downloading database...")

    file_id = "1-Recy6FYA8j8JlOHQ4Se1FUWdtvu8hrj"
    url = f"https://drive.google.com/uc?id={file_id}"

    try:
        gdown.download(url, file_path, quiet=False, fuzzy=True)
        print("✅ Download completed successfully!")
    except Exception as e:
        print("❌ ERROR: Unable to download file.")
        print("👉 Make sure file is public (Anyone with link).")
        print(e)
