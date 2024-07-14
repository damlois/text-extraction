import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path, pages):
    """
    Extracts text from specific pages of a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.
        pages (list of int): List of page numbers to extract text from.

    Returns:
        str: Extracted text from the specified pages of the PDF.
    """
    document = fitz.open(pdf_path)
    text = ""
    for page_num in pages:
        if page_num < 1 or page_num > len(document):
            print(f"Page number {page_num} is out of range. Skipping...")
            continue
        page = document.load_page(page_num - 1)  # PyMuPDF pages are 0-indexed
        text += page.get_text()
    return text

def save_text_to_file(text, output_path):
    """
    Saves text to a file.

    Args:
        text (str): Text to save.
        output_path (str): Path to the output text file.
    """
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

def main():
    pdf_path = input("Enter the path to the PDF file: ")
    if not os.path.isfile(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    output_path = input("Enter the path to save the extracted text: ")

    pages_input = input("Enter the page numbers to extract (comma-separated, e.g., 1,3,5): ")
    pages = [int(page.strip()) for page in pages_input.split(',')]

    # Extract text from specified pages of the PDF
    text = extract_text_from_pdf(pdf_path, pages)

    # Save the extracted text to a file
    save_text_to_file(text, output_path)

    print(f"Text extracted and saved to {output_path}")

if __name__ == "__main__":
    main()

