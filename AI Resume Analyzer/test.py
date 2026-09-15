from skill_detector import detect_skills

resume = """
I know Python, SQL, Power BI and Git.
"""

skills = detect_skills(resume)

print(skills)