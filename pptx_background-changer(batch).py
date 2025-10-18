#This script change background images of all pptx files in a folder to a specific image
# requirements: pip install python-pptx
import os
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches

def set_background_for_pptx(input_pptx, background_image, output_pptx):
    """
    Set a background image for all slides in a single PPTX file by adding the image to each slide.
    
    Args:
        input_pptx (str): Path to the input PPTX file
        background_image (str): Path to the background image file (e.g., .jpg, .png)
        output_pptx (str): Path where the modified PPTX will be saved
    """
    try:
        # Load the presentation
        prs = Presentation(input_pptx)
        
        # Get slide dimensions
        slide_width = prs.slide_width
        slide_height = prs.slide_height
        
        # Apply background image to each slide
        for slide in prs.slides:
            # Add the background image to the slide
            slide.shapes.add_picture(
                str(background_image),
                left=0,
                top=0,
                width=slide_width,
                height=slide_height
            )
            
            # Move the image to the back to act as a background
            picture = slide.shapes[-1]  # The newly added image
            slide.shapes._spTree.remove(picture._element)
            slide.shapes._spTree.insert(2, picture._element)  # Insert at the back
            
        # Save the modified presentation
        prs.save(output_pptx)
        print(f"Successfully set background for {input_pptx} and saved to {output_pptx}")
        
    except Exception as e:
        print(f"Error setting background for {input_pptx}: {str(e)}")

def batch_set_pptx_background(input_folder, background_image, output_folder):
    """
    Set a background image for all slides in all PPTX files in a folder.
    
    Args:
        input_folder (str): Path to folder containing PPTX files
        background_image (str): Path to the background image file
        output_folder (str): Path to folder where modified PPTX files will be saved
    """
    # Ensure input and output folders exist
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)
    
    # Validate background image
    background_image = Path(background_image)
    if not background_image.exists():
        print(f"Background image {background_image} does not exist.")
        return
    
    # Get all .pptx files in the input folder
    pptx_files = sorted(input_folder.glob("*.pptx"))  # Sort for consistent processing
    if not pptx_files:
        print(f"No .pptx files found in {input_folder}")
        return
    
    # Process each PPTX file
    for pptx_file in pptx_files:
        output_pptx = output_folder / f"{pptx_file.stem}_with_background.pptx"
        print(f"Processing {pptx_file}...")
        set_background_for_pptx(pptx_file, background_image, output_pptx)

if __name__ == "__main__":
    # Example usage
    input_folder = "/home/saidul/Desktop/Input"  # Your input folder path
    background_image = "/home/saidul/Desktop/background.jpeg"  # Replace with your background image path
    output_folder = "/home/saidul/Desktop/Output"  # Your output folder path
    
    if not os.path.exists(input_folder):
        print(f"Input folder {input_folder} does not exist.")
    else:
        batch_set_pptx_background(input_folder, background_image, output_folder)
