import pdfplumber
from docx import Document


def extract_text(file_path):
    """
    Extract text from PDF or DOCX file.
    """

    if file_path.endswith(".pdf"):
        text = ""

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

        return text

    elif file_path.endswith(".docx"):
        document = Document(file_path)

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text

    else:
        return "Unsupported File Type"