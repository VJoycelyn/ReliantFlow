import PyPDF2

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file for AI analysis.
    """
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        return f"Error extracting text: {e}"

if __name__ == "__main__":
    # Placeholder path for testing
    print("PDF Parser initialized and ready for contract ingestion.")
