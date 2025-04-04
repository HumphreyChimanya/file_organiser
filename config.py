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
        'documents': ['.pdf', '.docx', '.doc', '.txt'],
        'images': ['.jpg', '.jpeg', '.png', '.gif']
    }

    # Map file type to directory
    DESTINATION_MAP = {
        'music': MUSIC_DIR,
        'documents': DOCS_DIR,
        'images': IMAGES_DIR
    }
