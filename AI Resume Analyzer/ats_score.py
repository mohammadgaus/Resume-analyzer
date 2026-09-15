def calculate_ats_score(resume_text, detected_skills):
    score = 0

    # ----------------------------
    # Skills Score (Maximum 50)
    # ----------------------------
    score += min(len(detected_skills) * 10, 50)

    # ----------------------------
    # Resume Length (Maximum 20)
    # ----------------------------
    word_count = len(resume_text.split())

    if word_count >= 300:
        score += 20
    elif word_count >= 150:
        score += 10

    # ----------------------------
    # Important Sections (30)
    # ----------------------------
    sections = [
        "education",
        "experience",
        "project",
        "skills"
    ]

    resume_lower = resume_text.lower()

    for section in sections:
        if section in resume_lower:
            score += 7.5

    return round(score)