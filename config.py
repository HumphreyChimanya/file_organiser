import os

class Config:
    # Base path to scan
    SOURCE_DIR = os.path.expanduser("~/Downloads")  # Change this to wherever you're organizing

    # Target directories
    MUSIC_DIR = os.path.expanduser("~/Music")
    DOCS_DIR = os.path.expanduser("~/Documents")
    IMAGES_DIR = os.path.expanduser("~/Pictures")
    
    # File type mapping
    FILE_TYPES = {
        'music': ['.mp3', '.wav', '.flac'],
        'documents': ['.pdf', '.docx', '.doc', '.txt', '.py', '.pptx', '.java', .],
        'images': ['.jpg', '.jpeg', '.png', '.gif']
    }

    # Map file type to directory
    DESTINATION_MAP = {
        'music': MUSIC_DIR,
        'documents': DOCS_DIR,
        'images': IMAGES_DIR
    }
# config.py

# Base path to scan (can be empty, will be overridden by user input)
BASE_PATH = ""

# Target directory mapping (folder names for each file type)
TARGET_DIRS = {
    'Images': 'Images',
    'Documents': 'Documents',
    'Videos': 'Videos',
    'Audio': 'Audio',
    'Archives': 'Archives',
    'Code': 'Code',
    'Others': 'Others'
}

# File type mapping (extensions to category)
FILE_TYPE_MAPPING = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.tar'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp']
}
