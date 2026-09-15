def generate_suggestions(resume_text, detected_skills):
    suggestions = []

    # Resume Length
    if len(resume_text.split()) < 150:
        suggestions.append("Increase resume length.")

    # Skills
    if len(detected_skills) < 5:
        suggestions.append("Add more technical skills.")

    resume_lower = resume_text.lower()

    # Important Sections
    if "project" not in resume_lower:
        suggestions.append("Include a Projects section.")

    if "education" not in resume_lower:
        suggestions.append("Include an Education section.")

    if "experience" not in resume_lower:
        suggestions.append("Include an Experience section.")

    if "certification" not in resume_lower:
        suggestions.append("Add Certifications if applicable.")

    if not suggestions:
        suggestions.append("Excellent resume! Minor improvements only.")

    return suggestions