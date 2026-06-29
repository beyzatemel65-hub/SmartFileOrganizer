from pathlib import Path
import shutil
from datetime import datetime


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".pages"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Code": [".py", ".html", ".css", ".js"],
    "Archives": [".zip", ".rar", ".7z"],
}


def organize_folder(folder_path):
    folder = Path(folder_path)
    moved_files = []

    for file in folder.iterdir():
        if not file.is_file():
            continue

        if file.name.startswith("log_") or file.name == ".DS_Store":
            continue

        category_name = "Others"

        for category, extensions in FILE_CATEGORIES.items():
            if file.suffix.lower() in extensions:
                category_name = category
                break

        destination = folder / category_name
        destination.mkdir(exist_ok=True)

        shutil.move(str(file), str(destination / file.name))
        moved_files.append(f"{file.name} ➜ {category_name}")

    logs_folder = folder / "logs"
    logs_folder.mkdir(exist_ok=True)

    log_file = logs_folder / f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    with open(log_file, "w", encoding="utf-8") as log:
        log.write("Smart File Organizer Log\n")
        log.write("=" * 30 + "\n")
        log.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        log.write(f"Folder: {folder}\n")
        log.write(f"Total moved files: {len(moved_files)}\n\n")

        for item in moved_files:
            log.write(item + "\n")

    return moved_files, log_file