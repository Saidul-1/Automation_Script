# This script convert all pptx files of a folder to pdf file
# It uses libreoffice which usually available in linux-based OS
# Requirements { pip install PyPDF2 
#                sudo apt-get install libreoffice }
import os
from pathlib import Path
import subprocess

def batch_convert_pptx_to_pdf(input_folder, output_folder):
    """
    Batch convert all .pptx files in a folder to PDFs using LibreOffice.
    
    Args:
        input_folder (str): Path to folder containing .pptx files
        output_folder (str): Path to folder where PDFs will be saved
    """
    # Ensure input and output folders exist
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)
    
    # Get all .pptx files in the input folder
    pptx_files = sorted(input_folder.glob("*.pptx"))  # Sort to maintain sequence
    if not pptx_files:
        print(f"No .pptx files found in {input_folder}")
        return
    
    # Convert each .pptx to PDF using LibreOffice
    for pptx_file in pptx_files:
        output_pdf = output_folder / f"{pptx_file.stem}.pdf"
        print(f"Converting {pptx_file} to {output_pdf}...")
        try:
            # Run LibreOffice in headless mode to convert PPTX to PDF
            subprocess.run([
                "libreoffice",
                "--headless",
                "--convert-to",
                "pdf",
                "--outdir",
                str(output_folder),
                str(pptx_file)
            ], check=True)
            print(f"Successfully converted {pptx_file} to {output_pdf}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {pptx_file}: {str(e)}")

if __name__ == "__main__":
    input_folder = "/home/saidul/Desktop/Input"  # Replace with your input folder path
    output_folder = "/home/saidul/Desktop/Output"  # Replace with your output folder path
    
    if not os.path.exists(input_folder):
        print(f"Input folder {input_folder} does not exist.")
    else:
        batch_convert_pptx_to_pdf(input_folder, output_folder)
