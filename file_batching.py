#step1
#IMPORTS
import zipfile
import os
import shutil

#step2
#File Extractions and File Password
zip_file_path = "C:/Users/Anthony/Downloads/964AF7FC-A005-6154-E053-0100007F5B3E_attachments.zip"
extraction_path = "C:/Users/Anthony/Desktop/test_data"  #Use actual paths
txt_files_path = "C:/Users/Anthony/Desktop/txt_files"
bin_files_path = "C:/Users/Anthony/Desktop/bin_files"
password = b'N4u29l4YbuViQF8Uyqo9q4o8rlPRMGTj'  # Use the actual password here

#step3
# Create File Directories
os.makedirs(extraction_path, exist_ok=True)
os.makedirs(txt_files_path, exist_ok=True)
os.makedirs(bin_files_path, exist_ok=True)

#step4
# Extract the ZIP file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_path, pwd=password)

# Move .txt and .bin files to their respective directories
for root, dirs, files in os.walk(extraction_path):
    for file in files:
        if file.endswith('.txt'):
            shutil.move(os.path.join(root, file), os.path.join(txt_files_path, file))
        elif file.endswith('.bin'):
            shutil.move(os.path.join(root, file), os.path.join(bin_files_path, file))

print("Files have been organized successfully.")

#step5
#IMPORTS
import os
import shutil
import gzip

# Define the paths
main_directory_path = r"C:\Users\Anthony\Desktop\test_data\32354\1"  # Main directory containing individual folders
txt_files_path = r"C:\Users\Anthony\Desktop\txt_files"  # Directory to save .txt files

# Create the directory for .txt files if it doesn't exist
os.makedirs(txt_files_path, exist_ok=True)

# Iterate through each subfolder in the main directory
for subfolder_name in os.listdir(main_directory_path):
    subfolder_path = os.path.join(main_directory_path, subfolder_name)
    print(f"Checking subfolder: {subfolder_path}")  # Debug statement

    if os.path.isdir(subfolder_path):  # Check if it's a directory
        # Iterate through each file in the subfolder
        for filename in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, filename)
            if filename.endswith('.txt.gz'):
                print(f"Found .txt.gz file: {file_path}")  # Debug statement
                # Extract the .txt file
                with gzip.open(file_path, 'rb') as f_in:
                    txt_filename = filename[:-3]  # Remove the .gz extension
                    dest_path = os.path.join(txt_files_path, txt_filename)
                    with open(dest_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                print(f"Extracted and moved file: {file_path} to {dest_path}")  # Debug statement
            else:
                print(f"Not a .txt.gz file: {file_path}")  # Debug statement

print("All .txt.gz files have been extracted and organized successfully.")

#step6
import os

# Define the path to the directory containing .txt files
txt_files_path = r"C:\Users\Anthony\Desktop\txt_files"

# Count the number of .txt files in the directory
txt_file_count = len([file for file in os.listdir(txt_files_path) if file.endswith('.txt')])

print(f"There are {txt_file_count} .txt files in the directory: {txt_files_path}")

#step7
import os
import shutil

# Define the path to the directory containing .txt files
txt_files_path = r"C:\Users\Anthony\Desktop\txt_files"

# Define the base path for the batch directories
batch_base_path = r"C:\Users\Anthony\Desktop\txt_files_batches"

# Create the base directory for batches if it doesn't exist
os.makedirs(batch_base_path, exist_ok=True)

# Get all .txt files in the directory
txt_files = [f for f in os.listdir(txt_files_path) if f.endswith('.txt')]

# Break the files into batches of 50
batch_size = 50
for i in range(0, len(txt_files), batch_size):
    batch_files = txt_files[i:i + batch_size]
    batch_dir = os.path.join(batch_base_path, f"batch_{i // batch_size + 1}")
    os.makedirs(batch_dir, exist_ok=True)
    for file in batch_files:
        shutil.move(os.path.join(txt_files_path, file), os.path.join(batch_dir, file))

print("Files have been organized into batches of 50.")

#step8
import os

# Define the base path for the batch directories
batch_base_path = r"C:\Users\Anthony\Desktop\txt_files_batches"

# Iterate through each batch directory
for batch_dir in os.listdir(batch_base_path):
    batch_dir_path = os.path.join(batch_base_path, batch_dir)
    if os.path.isdir(batch_dir_path):
        # Iterate through each file in the batch directory
        for filename in os.listdir(batch_dir_path):
            file_path = os.path.join(batch_dir_path, filename)
            if os.path.getsize(file_path) == 0:  # Check if the file size is 0 KB
                print(f"Removing file: {file_path}")  # Debug statement
                os.remove(file_path)

print("0 KB files have been removed from all batches.")



