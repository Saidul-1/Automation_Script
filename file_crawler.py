# This script gather all the files of specific file types from all nested folders and store them in the output folder
import os
import shutil

# --- Configuration ---
# 1. Path to the main folder containing your 10 subfolders.
SOURCE_ROOT = r'/home/saidul/Desktop/4-1/AI/HandwrittenDigits/drive-download-20250906T193307Z-1-001' 

# 2. Path to the single folder where you want all images to go.
#    This folder will be created if it doesn't exist.
DESTINATION_FOLDER = r'/home/saidul/Desktop/4-1/AI/HandwrittenDigits/drive-download-20250906T193307Z-1-001/images'

# 3. Define which file types to look for.
IMAGE_EXTENSIONS = ('.jpg')
# --- End of Configuration ---


def consolidate_images():
    """
    Finds all images in a nested directory structure and moves them
    to a single destination folder, handling filename conflicts.
    """
    # Create the destination folder if it doesn't exist
    os.makedirs(DESTINATION_FOLDER, exist_ok=True)
    print(f"Destination folder ensured at: {DESTINATION_FOLDER}")
    
    moved_count = 0
    
    # Walk through the entire directory tree starting from the source root
    for dirpath, _, filenames in os.walk(SOURCE_ROOT):
        for filename in filenames:
            # Check if the file is an image based on its extension
            if filename.lower().endswith(IMAGE_EXTENSIONS):
                
                source_path = os.path.join(dirpath, filename)
                dest_path = os.path.join(DESTINATION_FOLDER, filename)
                
                # --- Handle potential filename conflicts ---
                counter = 1
                # If a file with the same name already exists in the destination...
                while os.path.exists(dest_path):
                    # ...create a new name by adding a number.
                    name, ext = os.path.splitext(filename)
                    new_filename = f"{name}_{counter}{ext}"
                    dest_path = os.path.join(DESTINATION_FOLDER, new_filename)
                    counter += 1
                
                # Move the file to the new, unique path
                shutil.move(source_path, dest_path)
                moved_count += 1
                print(f"Moved: {filename} -> {os.path.basename(dest_path)}")

    print(f"\n✅ Success! Moved a total of {moved_count} images to '{DESTINATION_FOLDER}'.")

if __name__ == "__main__":
    consolidate_images()
