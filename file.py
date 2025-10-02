import os
import shutil

# File type mapping
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".m4a", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".cpp", ".java"]
}

def organize_folder(path):
    if not os.path.isdir(path):
        print("Invalid path.")
        return

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            moved = False

            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    target_dir = os.path.join(path, folder)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_dir, file))
                    print(f"Moved '{file}' to '{folder}/'")
                    moved = True
                    break

            if not moved:
                others_dir = os.path.join(path, "Others")
                os.makedirs(others_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(others_dir, file))
                print(f"Moved '{file}' to 'Others/'")

if __name__ == "__main__":
    print("File Organizer")
    folder_path = input("Enter folder path to organize: ").strip()
    organize_folder(folder_path)
