import os
import shutil
from config import Config

def get_file_type(file_extension):
    for file_type, extensions in Config.FILE_TYPES.items():
        if file_extension.lower() in extensions:
            return file_type
    return None

def organize_files():
    for filename in os.listdir(Config.SOURCE_DIR):
        file_path = os.path.join(Config.SOURCE_DIR, filename)
        
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            file_type = get_file_type(ext)

            if file_type:
                destination_dir = Config.DESTINATION_MAP[file_type]
                os.makedirs(destination_dir, exist_ok=True)

                try:
                    shutil.move(file_path, os.path.join(destination_dir, filename))
                    print(f"Moved: {filename} → {destination_dir}")
                except Exception as e:
                    print(f"Failed to move {filename}: {e}")

if __name__ == "__main__":
    organize_files()
# organizer.py

import os
import shutil
import tkinter as tk
from tkinter import filedialog
from config import FILE_TYPE_MAPPING, TARGET_DIRS

def get_folder_path():
    print("Choose how to select the folder:")
    print("1. Enter path manually")
    print("2. Select folder using file dialog")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        folder = input("Enter the full path of the folder: ").strip()
    elif choice == '2':
        root = tk.Tk()
        root.withdraw()  # Hide the main tkinter window
        folder = filedialog.askdirectory(title="Select Folder to Organize")
    else:
        print("Invalid choice.")
        return None

    if not folder or not os.path.isdir(folder):
        print("That path doesn't exist or is not a folder.")
        return None

    return folder

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        src = os.path.join(folder_path, filename)

        if os.path.isfile(src):
            ext = os.path.splitext(filename)[1].lower()
            moved = False

            for category, extensions in FILE_TYPE_MAPPING.items():
                if ext in extensions:
                    dest_dir_name = TARGET_DIRS.get(category, category)
                    dest_folder = os.path.join(folder_path, dest_dir_name)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(src, os.path.join(dest_folder, filename))
                    moved = True
                    break

            if not moved:
                # Move to "Others" if no match
                other_folder = os.path.join(folder_path, TARGET_DIRS.get("Others", "Others"))
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(src, os.path.join(other_folder, filename))

if __name__ == "__main__":
    folder = get_folder_path()
    if folder:
        organize_files(folder)
        print(f"\nFiles in '{folder}' have been organized!")
    else:
        print("No folder selected. Exiting.")
