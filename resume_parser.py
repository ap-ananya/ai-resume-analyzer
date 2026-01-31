import PyPDF2
import docx

def extract_text(file):
    text = ""

    if file.filename.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()

    elif file.filename.endswith('.docx'):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + " "

    return text

def extract_sections(text):
    sections = {
        "skills": "",
        "experience": "",
        "education": ""
    }

    lines = text.lower().split("\n")
    current_section = None

    for line in lines:
        if "skill" in line:
            current_section = "skills"
        elif "experience" in line or "project" in line:
            current_section = "experience"
        elif "education" in line:
            current_section = "education"
        elif current_section:
            sections[current_section] += line + " "

    return sections
