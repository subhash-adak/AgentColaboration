import fitz
import docx
import io

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join([p.get_text() for p in doc])

def extract_text_from_docx(file):
    return "\n".join([p.text for p in docx.Document(io.BytesIO(file.read())).paragraphs])