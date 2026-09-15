from ats_score import calculate_ats_score

resume = """
Education

Experience

Projects

Skills

Python
SQL
Git
"""

skills = [
    "Python",
    "SQL",
    "Git"
]

score = calculate_ats_score(resume, skills)

print(score)