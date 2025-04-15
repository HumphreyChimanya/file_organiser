import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog
import json

from config import FILE_TYPE_MAPPING, TARGET_DIRS

# Prompt the user to either type a path or use a file dialog to select a folder
def get_folder_path():
    print("Choose how to select the folder:")
    print("1. Enter path manually")
    print("2. Select folder using file dialog")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        # Get folder path from user input
        folder = input("Enter the full path of the folder: ").strip()
    elif choice == '2':
        # Launch GUI folder picker using tkinter
        root = tk.Tk()
        root.withdraw()  # Hide the root tkinter window
        folder = filedialog.askdirectory(title="Select Folder to Organize")
    else:
        print("Invalid choice.")
        return None

    # Make sure the folder exists
    if not folder or not os.path.isdir(folder):
        print("That path doesn't exist or is not a folder.")
        return None

    return folder

# Helper function to convert bytes to KB/MB string
def format_size(bytes_size):
    kb = bytes_size / 1024
    if kb < 1024:
        return f"{kb:.2f} KB"
    return f"{kb / 1024:.2f} MB"

# Main function to organize files in a folder
def organize_files(folder_path):
    stats = {category: {'count': 0, 'size': 0} for category in TARGET_DIRS}
    undo_log = []  # 📝 Track original and new file paths
    start_time = time.time()

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
                    os.makedirs(dest_folder, exist_ok=True)
                    dest_path = os.path.join(dest_folder, filename)
                    
                    shutil.move(src, dest_path)
                    stats[category]['count'] += 1
                    stats[category]['size'] += file_size

                    undo_log.append({"from": dest_path, "to": src})  # 👈 Log the move
                    moved = True
                    break

            if not moved:

                category = ai_classify_file_content(src)
                print(f"[AI] {filename} classified as: {category}")
                other_folder = os.path.join(folder_path, TARGET_DIRS.get(category, category))
                os.makedirs(other_folder, exist_ok=True)
                dest_path = os.path.join(other_folder, filename)

                shutil.move(src, dest_path)
                stats[category]['count'] += 1
                stats[category]['size'] += file_size

                undo_log.append({"from": dest_path, "to": src})

    end_time = time.time()

    # Save undo log to disk
    with open(os.path.join(folder_path, ".undo_log.json"), "w") as f:
        json.dump(undo_log, f, indent=2)

    print_summary_report(stats, end_time - start_time)

    # Prompt for undo
    prompt_undo(folder_path)

def prompt_undo(folder_path):
    choice = input("\n⚠️ Would you like to undo the changes? (y/n): ").strip().lower()

    if choice == 'y':
        undo_file = os.path.join(folder_path, ".undo_log.json")
        if os.path.exists(undo_file):
            with open(undo_file, "r") as f:
                undo_log = json.load(f)

            for entry in undo_log:
                if os.path.exists(entry["from"]):
                    os.makedirs(os.path.dirname(entry["to"]), exist_ok=True)
                    shutil.move(entry["from"], entry["to"])

            os.remove(undo_file)
            print("✅ Undo complete! Files moved back to original locations.")
        else:
            print("❌ No undo log found. Nothing to undo.")
    else:
        print("✅ Changes kept. If needed, you can run undo later using the log.")


# Print a formatted summary of the organization process
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

# Program entry point
if __name__ == "__main__":
    folder = get_folder_path()
    if folder:
        organize_files(folder)
    else:
        print("No folder selected. Exiting.")

