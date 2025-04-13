import os

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
