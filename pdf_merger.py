# Merge all pdf files of a folder into one with natural ordering by name
# Requirements: pip install PyPDF2 natsort
import os
from pathlib import Path
import PyPDF2
from natsort import natsorted

def merge_pdfs_in_folder(input_folder, output_pdf_name="merged_output.pdf"):
    """
    Merge all PDF files in a folder into a single PDF, using natural ordering.
    
    Args:
        input_folder (str): Path to folder containing PDF files
        output_pdf_name (str): Name of the merged PDF file
    """
    # Ensure input folder exists
    input_folder = Path(input_folder)
    if not input_folder.exists():
        print(f"Input folder {input_folder} does not exist.")
        return
    
    # Get all .pdf files in the input folder, sorted with natural ordering
    pdf_files = natsorted(input_folder.glob("*.pdf"), key=str)
    if not pdf_files:
        print(f"No PDF files found in {input_folder}")
        return
    
    # Merge PDFs
    try:
        merger = PyPDF2.PdfMerger()
        for pdf in pdf_files:
            print(f"Adding {pdf} to merged output...")
            merger.append(str(pdf))
        output_path = input_folder / output_pdf_name
        merger.write(str(output_path))
        merger.close()
        print(f"Successfully merged PDFs into {output_path}")
    except Exception as e:
        print(f"Error merging PDFs: {str(e)}")

if __name__ == "__main__":
    # Example usage
    input_folder = "/home/saidul/Desktop/Input"  # Folder containing PDFs
    output_pdf_name = "merged_output.pdf"  # Name of the merged PDF file which will be saved in the input directory
    
    merge_pdfs_in_folder(input_folder, output_pdf_name)
