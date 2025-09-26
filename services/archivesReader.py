import os

def readAllPdfArchives(directory_path):
    archive_extensions = [".pdf"]
    archive_files = []
    for filename in os.listdir(directory_path):
        full_path = os.path.join(directory_path, filename)
        if os.path.isfile(full_path):  # Check if it's a file (not a directory)
            # Check if the file extension is in the list of archive extensions
            if any(filename.lower().endswith(ext) for ext in archive_extensions):
                archive_files.append(directory_path+"/"+filename)
    return archive_files