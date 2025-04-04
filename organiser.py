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
