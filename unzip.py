#All pre-installed python modules
import zipfile
import os
import tkinter as tk
from tkinter import filedialog
import shutil
import glob

#Nice Progress bar, have to install seperately :))
from tqdm import tqdm

#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~

#Define functions:

def has_subfolders(directory):
    #check if it contains any subfolders
    for _, dirs, _ in os.walk(directory):
        if dirs:  # If there are subdirectories
            return True
    return False

def check_subfolders(directory):
    # Traverse the directory structure and check each folder
    folder_status = {}
    for root, dirs, _ in os.walk(directory):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            folder_status[folder_path] = has_subfolders(folder_path)
    return folder_status

def move_folder(src_folder, dest_folder):
    # Move the folder from src to dest
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # Create the destination folder if it doesn't exist
    shutil.move(src_folder, dest_folder)

# Function to open files
def select_files(prompt):
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(title=prompt, filetypes=[("ZIP files", "*.zip")])
    return file_paths

# Function to open folder
def select_folder(prompt):
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title=prompt)
    return folder_path

def extractor(zips, temp):
    #Extract all of the data into a temp folder
    for zip_file in zips:
        print("")
        try:
            with zipfile.ZipFile(zip_file, 'r') as zf:
                for member in tqdm(zf.infolist(), desc=f'Extracting {os.path.basename(zip_file)}'):
                    try:
                        zf.extract(member, temp)
                
                    except zipfile.error as e:
                        print(f"Error extracting {member.filename}: {e}")
        except zipfile.BadZipFile:
                    print(f"{zip_file} is not a valid zip file. Skipping...")

#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~
#main function

def main():
    #select the source .zip files
    zip_files = select_files("Select the ZIP files to extract:")
    if not zip_files:
        print("No files selected. Exiting...")
        return

    #select the destination directory for unzipped files
    unzipped_dir = select_folder("Select the destination directory for extracted files:")
    if not unzipped_dir:
        print("No directory selected. Exiting...")
        return

    #make a temp directry in the pwd
    temp = 'TeMp/'
    #If it doesn't exist, make it  
    if not os.path.isdir(temp):
         os.makedirs(temp)  
    #If it does exist, remove its contents  
    shutil.rmtree(temp)
    
    #Extract data
    extractor(zip_files, temp)
    
    #Loop over all subfolders, move all of the data we want
    for folder, has_subfolder in check_subfolders(temp).items():
        if not has_subfolder:
            move_folder(folder, unzipped_dir)

    #Remove the temp folder
    shutil.rmtree(temp, ignore_errors=True)

    print("")
    #This is more of a sanity check than anything else.
    print(f"Extracted: {len(glob.glob(f'{unzipped_dir}/*')):,} lines of data.")
    print("CHECK WITH SCREENING EAGLE PLS")
    print("")

if __name__ == "__main__":
    main()
