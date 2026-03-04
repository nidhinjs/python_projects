import os
import shutil

FOLDER_MAP = {
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.svg': 'Images',
    '.webp': 'Images',

    '.pdf': 'My Docs',
    '.docx': 'My Docs',
    '.doc': 'My Docs',
    '.txt': 'My Docs',
    '.xlsx': 'My Docs',
    '.pptx': 'My Docs',
    '.csv': 'My Docs',

    '.mp4': 'Vids',
    '.mov': 'Vids',
    '.avi': 'Vids',
    '.mkv': 'Vids',

    '.mp3': 'Sounds',
    '.wav': 'Sounds',
    '.flac': 'Sounds',
    '.aac': 'Sounds',

    '.zip': 'Archive',
    '.rar': 'Archive',
    '.7z': 'Archive',
    '.tar': 'Archive',

    '.exe': 'Programs',
    '.msi': 'Programs',

    '.py': 'Code',
    '.js': 'Code',
    '.html': 'Code',
    '.css': 'Code',
    '.json': 'Code',
}

DOWNLOADS = r"C:\Users\HP\Downloads"

def organize():
    for filename in os.listdir(DOWNLOADS):
      fullpath = os.path.join(DOWNLOADS, filename)     

        if os.path.isdir(fullpath):
            continue

        extension = os.path.splitext(filename)[1].lower()

        destination_folder = FOLDER_MAP.get(extension, 'Misc')

        destination_path = os.path.join(DOWNLOADS, destination_folder)
        destination_file = os.path.join(destination_path, filename)

        os.makedirs(destination_path, exist_ok=True)

        if os.path.exists(destination_file):
            os.remove(destination_file)

        shutil.move(fullpath, destination_file)
        print(f'Moved {filename} → {destination_folder}/')

print("\nOrganizing Downloads Folder\n")
organize()
print("\nDone :)")
