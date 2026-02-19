# Multi-Candidate Intelligent Resume Analyzer (CLI)

## 📌 Project Overview
This is a CLI-based Multi-Candidate Intelligent Resume Analyzer developed using Python.  
The application analyzes multiple resumes in PDF form, extracts essential details, computes skill matching scores, ranks candidates, and provides a formatted JSON report.

---

## 🚀 Features

- 📄 PDF Resume Parsing
- 👤 Name Extraction
- 📧 Email Extraction
- 💼 Experience Detection
- 🎯 Skill Matching Algorithm
- 📊 0–100 Resume Score Calculation
- 🏆 Candidate Ranking System
- 📝 Hiring Recommendation
- 📂 JSON Report Generation
- 🔁 Multi-Candidate Support

---

## 🛠 Technologies Used

- Python
- PyPDF2 (PDF parsing)
- Regular Expressions (Regex)
- JSON module

---

## ⚙️ How It Works

1. Enter required skills (comma separated).
2. Upload multiple resume PDFs.
3. System extracts resume data.
4. Matches required skills.
5. Calculates score (matched/total × 100).
6. Ranks candidates based on score.
7. Saves final report in `all_candidates_report.json`.

---

## 📊 Scoring Algorithm

Score = (Number of Matched Skills / Total Required Skills) × 100

---

## 📂 Project Structure
---

## ⚙️ Setup Guide

1. Clone the repository:
git clone <repository_link>

2. Navigate into the project folder:
cd intelligent_resume_analyzer_hidevs

3. Install required dependencies:
pip install -r requirements.txt

4. Run the program:
python main.py

---

## 📁 Project Structure

main.py          → Controls program flow and multi-candidate logic  
utils.py         → Contains parsing, matching, and scoring functions  
requirements.txt → Required Python dependency  
README.md        → Project documentation  

---

## 🎥 Demo Video

YouTube Demo Link: 





Hanish Aradhya G  
B.Tech AIML
Reva University

