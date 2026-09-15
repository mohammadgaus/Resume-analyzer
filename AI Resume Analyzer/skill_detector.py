import json


def detect_skills(resume_text):
    """
    Detect skills present in the resume.
    """

    with open("data/skills.json", "r") as file:
        skills = json.load(file)

    found_skills = []

    resume_lower = resume_text.lower()

    for skill in skills:

        if skill.lower() in resume_lower:
            found_skills.append(skill)

    return found_skills