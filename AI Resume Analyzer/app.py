from pydoc import text

import customtkinter as ctk
from tkinter import filedialog
from parser import extract_text
from skill_detector import detect_skills
from ats_score import calculate_ats_score
from suggestions import generate_suggestions

# ----------------------------
# App Configuration
# ----------------------------
ctk.set_appearance_mode("System")   # Options: Light, Dark, System
ctk.set_default_color_theme("blue")

# ----------------------------
# Main Window
# ----------------------------
app = ctk.CTk()

app.title("AI Resume Analyzer")
app.geometry("1000x650")
app.minsize(900, 600)

# ----------------------------
# Sidebar
# ----------------------------
sidebar = ctk.CTkFrame(app, width=250, corner_radius=0)
sidebar.pack(side="left", fill="y")

# Sidebar Title
title = ctk.CTkLabel(
    sidebar,
    text="AI Resume\nAnalyzer",
    font=("Arial", 24, "bold")
)

title.pack(pady=30)

# ----------------------------
# Upload Resume Function
# ----------------------------
def upload_resume():
    file_path = filedialog.askopenfilename(
        title="Select Resume",
        filetypes=[
            ("PDF Files", "*.pdf"),
            ("Word Documents", "*.docx")
        ]
    )

    if file_path:
        text = extract_text(file_path)
        skills = detect_skills(text)
        score = calculate_ats_score(text, skills)
        print(skills)
        print(score)
        resume_textbox.configure(state="normal")
        # Clear previous resume
        resume_textbox.delete("1.0", "end")

        # Display extracted text
        if text.strip():
            resume_textbox.insert("1.0", text)
        else:
            resume_textbox.insert(
                "1.0",
                "No readable text found in the resume."
            )
        # ----------------------------
        # Suggestions Section
        # ----------------------------
        resume_textbox.insert("end", "\n\n")
        resume_textbox.insert("end", "=" * 50 + "\n")
        resume_textbox.insert("end", "RESUME SUGGESTIONS\n")
        resume_textbox.insert("end", "=" * 50 + "\n\n")

        suggestions = generate_suggestions(text, skills)

        for suggestion in suggestions:
            resume_textbox.insert("end", f"• {suggestion}\n")

        resume_textbox.configure(state="disabled")

        if skills:
            skills_label.configure(
                text="\n".join(f" {skill}" for skill in skills)
            )
        else:
            skills_label.configure(
                text="No matching skills found."
            )

        ats_score_label.configure(
            text=f"{score}%"
        )
        ats_progress.set(score / 100)

        suggestions_label.configure(state="disabled")
# ----------------------------
# Upload Button
# ----------------------------
upload_btn = ctk.CTkButton(
    sidebar,
    text="Upload Resume",
    width=180,
    command=upload_resume
)

upload_btn.pack(pady=15)

# ----------------------------
# Main Content Area
# ----------------------------
content = ctk.CTkFrame(app,corner_radius=10)
content.pack(side="right", fill="both", expand=True, padx=10, pady=10)
top_frame = ctk.CTkFrame(content)

top_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=15
)
# ----------------------------
# Content Title
# ----------------------------
content_title = ctk.CTkLabel(
    top_frame,
    text="Resume Content",
    font=("Arial", 24, "bold")
)

content_title.pack(pady=20)

resume_textbox = ctk.CTkTextbox(
    top_frame,
    width=700,
    height=500,
    font=("Consolas", 14)
)
resume_textbox.pack(
    padx=20, 
    pady=10, 
    fill="both", 
    expand=True
)
resume_textbox.configure(state="disabled")
bottom_frame = ctk.CTkFrame(
    content,
    height=450
)

bottom_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=(0, 15)
)

skills_frame = ctk.CTkFrame(
    bottom_frame
)

skills_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 5)
)

# ----------------------------
# ATS Panel
# ----------------------------
ats_frame = ctk.CTkFrame(
    bottom_frame
)

ats_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=(5, 0)
)

# ----------------------------
# ATS Title
# ----------------------------
ats_title = ctk.CTkLabel(
    ats_frame,
    text="ATS Score",
    font=("Arial", 20, "bold")
)

ats_title.pack(pady=(15, 10))

ats_score_label = ctk.CTkLabel(
    ats_frame,
    text="0%",
    font=("Arial", 40, "bold")
)

ats_score_label.pack(pady=10)

# ----------------------------
# ATS Progress Bar
# ----------------------------
ats_progress = ctk.CTkProgressBar(
    ats_frame,
    width=220
)

ats_progress.pack(pady=10)

# Initial value
ats_progress.set(0)

suggestions_title = ctk.CTkLabel(
    ats_frame,
    text="Suggestions",
    font=("Arial", 18, "bold")
)

suggestions_title.pack(pady=(5, 2))
print("Suggestions title created")

suggestions_label = ctk.CTkTextbox(
    ats_frame,
    width=250,
    height=450
)

suggestions_label.pack(
    padx=20,
    pady=10,
    fill="both",
    expand=True
)
print("Suggestions textbox created")

skills_title = ctk.CTkLabel(
    skills_frame,
    text="Detected Skills",
    font=("Arial", 20, "bold")
)

skills_title.pack(pady=(10, 10))

# ----------------------------
# Skills Label
# ----------------------------
skills_label = ctk.CTkLabel(
    skills_frame,
    text="No skills detected.",
    justify="left",
    anchor="nw"
)

skills_label.pack(padx=20, pady= 10,anchor="nw")

suggestions_label.insert(
    "1.0",
    "THIS IS A TEST"
)
suggestions_label.configure(state="disabled")
print("Textbox width :", suggestions_label.winfo_reqwidth())
print("Textbox height:", suggestions_label.winfo_reqheight())

# ----------------------------
# Run Application
# ----------------------------
app.mainloop()