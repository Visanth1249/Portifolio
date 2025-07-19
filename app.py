from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/certifications")
def certifications():
    return render_template("certifications.html")

@app.route("/internships")
def internships():
    return render_template("internships.html")

@app.route("/achievements")
def achievements():
    return render_template("achievements.html")

@app.route("/resume")
def resume():
    return send_from_directory("resume", "Visanth_final_updated_resume 1.pdf", as_attachment=False)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

