# This script converts all images of a folder to pure grayscale/binary image: each pixel is either pure white or pure black.
import os
from PIL import Image

# --- Configuration ---
# 1. Path to the directory containing your 5300 images.
SOURCE_FOLDER = r'/home/saidul/Desktop/4-1/AI/HandwrittenDigits/drive-download-20250906T193307Z-1-001/images'

# 2. Path to the folder where processed images will be saved.
#    This folder will be created automatically if it doesn't exist.
OUTPUT_FOLDER = r'/home/saidul/Desktop/4-1/AI/HandwrittenDigits/drive-download-20250906T193307Z-1-001/processed_images'

# 3. Define which file types to process.
IMAGE_EXTENSIONS = ('.jpg')
# --- End of Configuration ---


def process_image(input_path: str, output_path: str):
    """
    Resizes an image to 28x28 and converts it to a binary format.
    Returns True on success, False on failure.
    """
    try:
        # Open the image
        img = Image.open(input_path)

        # Step 1: Convert to grayscale ('L' mode) for thresholding
        img_gray = img.convert('L')

        # Step 2: Binarize the image using a 50% threshold (128)
        # .convert('1') creates a true 1-bit black and white image
        binary_img = img_gray.point(lambda p: 0 if p < 128 else 255, '1')
        
        # Step 3: Save the processed image
        binary_img.save(output_path)
        return True
        
    except Exception as e:
        print(f"--> Could not process {os.path.basename(input_path)} due to error: {e}")
        return False


def batch_process_images():
    """
    Loops through all images in the source folder and processes them.
    """
    # Create the output folder if it doesn't exist
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    print(f"Starting batch process...")
    print(f"Source: {SOURCE_FOLDER}")
    print(f"Output: {OUTPUT_FOLDER}\n")
    
    all_files = os.listdir(SOURCE_FOLDER)
    image_files = [f for f in all_files if f.lower().endswith(IMAGE_EXTENSIONS)]
    
    total_images = len(image_files)
    if total_images == 0:
        print("No images found in the source folder. Exiting.")
        return

    processed_count = 0
    
    for i, filename in enumerate(image_files):
        # Construct full input and output paths
        input_path = os.path.join(SOURCE_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)
        
        # Process the individual image
        if process_image(input_path, output_path):
            processed_count += 1
        
        # Print progress update
        print(f"Progress: {i + 1}/{total_images} | Processed: {filename}")

    print(f"\n✅ Batch process complete!")
    print(f"Successfully processed {processed_count} out of {total_images} images.")


if __name__ == "__main__":
    batch_process_images()
