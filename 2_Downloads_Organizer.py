import os
import shutil

FOLDER_MAP = {
    # 🖼️ Images
    '.jpg':  '🖼️ Images',
    '.jpeg': '🖼️ Images',
    '.png':  '🖼️ Images',
    '.gif':  '🖼️ Images',
    '.svg':  '🖼️ Images',
    '.webp': '🖼️ Images',
    '.bmp':  '🖼️ Images',
    '.tiff': '🖼️ Images',
    '.tif':  '🖼️ Images',
    '.ico':  '🖼️ Images',
    '.heic': '🖼️ Images',
    '.avif': '🖼️ Images',
    '.raw':  '🖼️ Images',

    # 📄 Documents
    '.pdf':  '📄 My Docs',
    '.docx': '📄 My Docs',
    '.doc':  '📄 My Docs',
    '.txt':  '📄 My Docs',
    '.xlsx': '📄 My Docs',
    '.xls':  '📄 My Docs',
    '.pptx': '📄 My Docs',
    '.ppt':  '📄 My Docs',
    '.csv':  '📄 My Docs',
    '.odt':  '📄 My Docs',
    '.ods':  '📄 My Docs',
    '.odp':  '📄 My Docs',
    '.rtf':  '📄 My Docs',
    '.md':   '📄 My Docs',
    '.epub': '📄 My Docs',
    '.pages':'📄 My Docs',
    '.numbers': '📄 My Docs',
    '.keynote': '📄 My Docs',

    # 🎬 Videos
    '.mp4':  '🎬 Vids',
    '.mov':  '🎬 Vids',
    '.avi':  '🎬 Vids',
    '.mkv':  '🎬 Vids',
    '.wmv':  '🎬 Vids',
    '.flv':  '🎬 Vids',
    '.webm': '🎬 Vids',
    '.m4v':  '🎬 Vids',
    '.3gp':  '🎬 Vids',
    '.ts':   '🎬 Vids',
    '.vob':  '🎬 Vids',

    # 🎵 Audio
    '.mp3':  '🎵 Sounds',
    '.wav':  '🎵 Sounds',
    '.flac': '🎵 Sounds',
    '.aac':  '🎵 Sounds',
    '.ogg':  '🎵 Sounds',
    '.m4a':  '🎵 Sounds',
    '.wma':  '🎵 Sounds',
    '.opus': '🎵 Sounds',
    '.aiff': '🎵 Sounds',
    '.mid':  '🎵 Sounds',
    '.midi': '🎵 Sounds',

    # 🗜️ Archives
    '.zip':  '🗜️ Archive',
    '.rar':  '🗜️ Archive',
    '.7z':   '🗜️ Archive',
    '.tar':  '🗜️ Archive',
    '.gz':   '🗜️ Archive',
    '.bz2':  '🗜️ Archive',
    '.xz':   '🗜️ Archive',
    '.tgz':  '🗜️ Archive',
    '.zst':  '🗜️ Archive',
    '.cab':  '🗜️ Archive',
    '.iso':  '🗜️ Archive',
    '.dmg':  '🗜️ Archive',

    # ⚙️ Programs
    '.exe':  '⚙️ Programs',
    '.msi':  '⚙️ Programs',
    '.app':  '⚙️ Programs',
    '.pkg':  '⚙️ Programs',
    '.deb':  '⚙️ Programs',
    '.rpm':  '⚙️ Programs',
    '.apk':  '⚙️ Programs',
    '.bat':  '⚙️ Programs',
    '.sh':   '⚙️ Programs',
    '.cmd':  '⚙️ Programs',

    # 💻 Code
    '.py':   '💻 Code',
    '.js':   '💻 Code',
    '.ts':   '💻 Code',
    '.jsx':  '💻 Code',
    '.tsx':  '💻 Code',
    '.html': '💻 Code',
    '.css':  '💻 Code',
    '.scss': '💻 Code',
    '.sass': '💻 Code',
    '.json': '💻 Code',
    '.xml':  '💻 Code',
    '.yaml': '💻 Code',
    '.yml':  '💻 Code',
    '.toml': '💻 Code',
    '.sql':  '💻 Code',
    '.php':  '💻 Code',
    '.rb':   '💻 Code',
    '.rs':   '💻 Code',
    '.go':   '💻 Code',
    '.java': '💻 Code',
    '.c':    '💻 Code',
    '.cpp':  '💻 Code',
    '.cs':   '💻 Code',
    '.swift':'💻 Code',
    '.kt':   '💻 Code',
    '.lua':  '💻 Code',
    '.r':    '💻 Code',

    # 🖋️ Fonts
    '.ttf':  '🖋️ Fonts',
    '.otf':  '🖋️ Fonts',
    '.woff': '🖋️ Fonts',
    '.woff2':'🖋️ Fonts',
    '.eot':  '🖋️ Fonts',

    # 🗄️ Data
    '.db':   '🗄️ Data',
    '.sqlite': '🗄️ Data',
    '.sql':  '🗄️ Data',
    '.json': '🗄️ Data',
    '.parquet': '🗄️ Data',
    '.hdf5': '🗄️ Data',
    '.h5':   '🗄️ Data',

    # 🔑 Keys & Config
    '.env':  '🔑 Config',
    '.ini':  '🔑 Config',
    '.cfg':  '🔑 Config',
    '.conf': '🔑 Config',
    '.pem':  '🔑 Config',
    '.key':  '🔑 Config',
    '.cert': '🔑 Config',
    '.crt':  '🔑 Config',
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
