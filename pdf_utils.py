# pdf_utils.py
import PyPDF2

def extract_text_from_pdf(uploaded_file) -> str:
    # uploaded_file is a Streamlit UploadedFile object or an open file-like object
    try:
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for p in reader.pages:
            page_text = p.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    except Exception as e:
        return f"Error extracting PDF: {e}"
