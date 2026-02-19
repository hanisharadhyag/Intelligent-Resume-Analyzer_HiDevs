from utils import (
    extract_text_from_pdf,
    clean_text,
    extract_keywords,
    calculate_score,
    extract_email,
    extract_name,
    extract_experience,
    save_report_to_json
)

def main():
    print("===== Multi-Candidate Intelligent Resume Analyzer =====")

    # Take required skills once
    required_skills = input("Enter required skills (comma separated): ").strip()
    skills_list = [skill.strip() for skill in required_skills.split(",") if skill.strip()]

    if not skills_list:
        print("No skills entered. Exiting.")
        return

    candidates = []

    while True:
        file_path = input("\nEnter Resume PDF file path: ").strip().strip('"')

        try:
            resume_text = extract_text_from_pdf(file_path)
        except Exception as e:
            print("Error reading file:", e)
            continue

        if not resume_text:
            print("Resume text could not be extracted.")
            continue

        name = extract_name(resume_text)
        email = extract_email(resume_text)
        experience = extract_experience(resume_text)

        cleaned_text = clean_text(resume_text)

        score, matched_skills, missing_skills = calculate_score(cleaned_text, skills_list)
        keywords = extract_keywords(cleaned_text)

        # Hiring recommendation
        if score >= 70:
            recommendation = "Strongly Recommended"
        elif score >= 40:
            recommendation = "Consider for Interview"
        else:
            recommendation = "Not Recommended"

        candidate_data = {
            "Name": name,
            "Email": email,
            "Experience (Years)": experience,
            "Resume Score": round(score, 2),
            "Matched Skills": matched_skills,
            "Missing Skills": missing_skills,
            "Top Keywords": keywords,
            "Recommendation": recommendation
        }

        candidates.append(candidate_data)

        print(f"\n{name} analyzed successfully!")
        print(f"Score: {round(score,2)}% | Recommendation: {recommendation}")

        another = input("Analyze another resume? (y/n): ").lower()
        if another != 'y':
            break

    # Sort candidates by score (highest first)
    candidates.sort(key=lambda x: x["Resume Score"], reverse=True)

    print("\n===== Candidate Rankings =====")
    for index, candidate in enumerate(candidates, start=1):
        print(f"{index}. {candidate['Name']} - {candidate['Resume Score']}%")

    # Save all candidates report
    save_report_to_json(candidates, "all_candidates_report.json")

    print("\nAll reports saved as all_candidates_report.json")


if __name__ == "__main__":
    main()
