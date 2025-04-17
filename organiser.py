import os
import shutil
import time
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
        root.withdraw()
        folder = filedialog.askdirectory(title="Select Folder to Organize")
    else:
        print("Invalid choice.")
        return None

    if not folder or not os.path.isdir(folder):
        print("That path doesn't exist or is not a folder.")
        return None

    return folder

def format_size(bytes_size):
    kb = bytes_size / 1024
    if kb < 1024:
        return f"{kb:.2f} KB"
    return f"{kb / 1024:.2f} MB"

# Plan what changes would be made without applying them
def get_planned_moves(folder_path):
    planned = []

    for filename in os.listdir(folder_path):
        src = os.path.join(folder_path, filename)
        if os.path.isfile(src):
            ext = os.path.splitext(filename)[1].lower()
            file_size = os.path.getsize(src)
            moved = False

            for category, extensions in FILE_TYPE_MAPPING.items():
                if ext in extensions:
                    dest_dir_name = TARGET_DIRS.get(category, category)
                    dest_folder = os.path.join(folder_path, dest_dir_name)
                    dest_path = os.path.join(dest_folder, filename)
                    planned.append((filename, src, dest_path, category, file_size))
                    moved = True
                    break

            if not moved:
                category = 'Others'
                dest_folder = os.path.join(folder_path, TARGET_DIRS.get(category, category))
                dest_path = os.path.join(dest_folder, filename)
                planned.append((filename, src, dest_path, category, file_size))

    return planned

def organize_files(folder_path, planned_moves):
    stats = {category: {'count': 0, 'size': 0} for category in TARGET_DIRS}
    start_time = time.time()

    for filename, src, dest, category, size in planned_moves:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.move(src, dest)
        stats[category]['count'] += 1
        stats[category]['size'] += size

    end_time = time.time()
    print_summary_report(stats, end_time - start_time)

def print_summary_report(stats, duration):
    print("\n📊 Summary Report:")
    total_files = 0
    total_size = 0
    for category, data in stats.items():
        if data['count'] > 0:
            print(f" - {category}: {data['count']} file(s), {format_size(data['size'])}")
            total_files += data['count']
            total_size += data['size']

    print(f"\n✅ Total files organized: {total_files}")
    print(f"💾 Total size organized: {format_size(total_size)}")
    print(f"⏱ Time taken: {duration:.2f} seconds")

def review_and_confirm(folder_path):
    planned_moves = get_planned_moves(folder_path)

    if not planned_moves:
        print("✅ No files to organize.")
        return

    print("\n🔍 Planned File Organization:\n")
    for filename, _, dest, category, size in planned_moves:
        print(f" - {filename} → {category}/ ({format_size(size)})")

    confirm = input("\n⚠️ Do you want to apply these changes? (y/n): ").strip().lower()
    if confirm == 'y':
        organize_files(folder_path, planned_moves)
    else:
        print("❌ No changes were made.")

if __name__ == "__main__":
    folder = get_folder_path()
    if folder:
        review_and_confirm(folder)
    else:
        print("No folder selected. Exiting.")
