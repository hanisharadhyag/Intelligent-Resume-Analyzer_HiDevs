import PyPDF2
import re

# Extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


# Clean text
def clean_text(text):
    return text.lower()


# Extract top 5 keywords
def extract_keywords(text):
    words = text.split()
    return words[:5]


# Improved skill matching
def calculate_score(resume_text, required_skills):
    resume_text = resume_text.lower()

    resume_words = set(re.findall(r'\b\w+\b', resume_text))

    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        skill = skill.lower().strip()
        if skill in resume_words:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(required_skills) == 0:
        return 0, matched_skills, missing_skills

    score = (len(matched_skills) / len(required_skills)) * 100

    return score, matched_skills, missing_skills
# Extract email using regex
def extract_email(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+'
    match = re.search(pattern, text)
    return match.group(0) if match else "Not Found"


# Extract name (simple logic: first non-empty line)
def extract_name(text):
    lines = text.split("\n")
    for line in lines:
        if line.strip() != "":
            return line.strip()
    return "Not Found"

import json

def save_report_to_json(data, filename="report.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Extract years of experience
def extract_experience(text):
    import re
    pattern = r'(\d+)\s+year'
    matches = re.findall(pattern, text.lower())

    if matches:
        total_years = sum(int(year) for year in matches)
        return total_years
    return 0



