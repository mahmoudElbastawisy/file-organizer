from pathlib import Path
import shutil

# Change this to the folder you want to organize
TARGET_FOLDER = Path.home() / "Desktop" / "test_folder"

# File type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Documents": [".doc", ".docx", ".txt", ".csv", ".xlsx", ".ppt", ".pptx"],
    "Archives": [".zip", ".rar", ".7z"],
}

def get_category(file_extension: str) -> str:
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder: Path) -> None:
    if not folder.exists() or not folder.is_dir():
        print(f"Folder does not exist: {folder}")
        return

    moved_files = 0

    for item in folder.iterdir():
        if item.is_file():
            category = get_category(item.suffix)
            category_folder = folder / category
            category_folder.mkdir(exist_ok=True)

            destination = category_folder / item.name

            # Handle duplicate names
            counter = 1
            while destination.exists():
                destination = category_folder / f"{item.stem}_{counter}{item.suffix}"
                counter += 1

            shutil.move(str(item), str(destination))
            print(f"Moved: {item.name} -> {category}/")
            moved_files += 1

    print(f"\nDone. Total files moved: {moved_files}")

if __name__ == "__main__":
    organize_folder(TARGET_FOLDER)