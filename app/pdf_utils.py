from pypdf import PdfReader
from typing import List
from io import BytesIO




def extract_text_from_pdf(file):
    read = PdfReader(file)
    texts = ' '
    for page in read.pages:
        texts += page.extract_text() or ''
    return texts