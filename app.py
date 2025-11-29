from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = {
        "name": "Sanjay R",
        "age": 18,
        "location": "Kulanada, Pandalam",
        "education": "1st Semester B.Tech CSE at Amal Jyothi College of Engineering",
        "school": "Passed 12th in 2025 – Amrita Vidyalayam, Pandalam",

        "bio": "I’m a first-year CSE student who is consistently passionate about learning how technology works. I enjoy building small projects that improve my logic and help me grow as a developer. Currently exploring Python, Java and UI designing with Figma.",

        "skills": [
            "Python (Intermediate — Strengthening Logic with Functions, Classes & Real Use-Cases)",
            "Java (Beginner — Exploring Basics & OOP Foundations)",
            "Figma (UI/UX — Wireframing & Simple Interface Design)"
        ],

        "projects": [
            {
                "name": "Rock–Paper–Scissors (Python)",
                "desc": "A fun console-based game built to practice conditionals, loops, and the random module."
            }
        ],

        "links": {
            "Email": "sanjayr2029@cs.ajce.in",
            "Instagram": "https://www.instagram.com/_.sanjay.r",
            "LinkedIn": "https://www.linkedin.com/in/sanjay-r-9b0440387"
        }
    }

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
