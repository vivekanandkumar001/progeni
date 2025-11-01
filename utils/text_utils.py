from PyPDF2 import PdfReader
import docx2txt

def extract_text_from_pdf(path):
    text = []
    reader = PdfReader(path)
    for p in reader.pages:
        t = p.extract_text()
        if t:
            text.append(t)
    return "\n".join(text)

def extract_text_from_docx(path):
    return docx2txt.process(path)
