# This script resize and convert all images of a folder into square shape using padding when necessary to preserve the aspect ratio
from PIL import Image
import os

target_size = 224
def make_square_image(input_path, output_path, fill_color=(255, 255, 255)):
    """
    Resizes the image proportionally so the longer side is target_size,
    then pads the shorter side with fill_color to make it square.
    """
    with Image.open(input_path) as img:
        # Calculate scaling factor for proportional resize
        width, height = img.size
        if width > height:
            new_width = target_size
            new_height = int((height / width) * target_size)
        else:
            new_height = target_size
            new_width = int((width / height) * target_size)
        
        # Resize proportionally
        img = img.resize((new_width, new_height), Image.LANCZOS)
        
        # Create a new square image with white background
        square_img = Image.new("RGB", (target_size, target_size), fill_color)
        
        # Paste the resized image centered in the square
        paste_x = (target_size - new_width) // 2
        paste_y = (target_size - new_height) // 2
        square_img.paste(img, (paste_x, paste_y))
        
        # Save the result
        square_img.save(output_path)

# Batch process all images in a folder
input_folder = "/home/saidul/Desktop/Input"  # Replace with your input folder
output_folder = "/home/saidul/Desktop/Output"  # Replace with your output folder
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"{target_size}x{target_size}_{filename}")
        make_square_image(input_path, output_path)
        print(f"Processed {filename} -> {output_path}")
