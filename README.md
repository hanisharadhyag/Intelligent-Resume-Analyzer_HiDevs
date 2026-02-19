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
