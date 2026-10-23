
from flask import Flask, render_template, url_for
import uuid

app = Flask(__name__)


# Static routes: render resume.html
@app.route("/")
@app.route("/home")
def home():
    return render_template("resume.html")


# Static route: About page
@app.route("/about")
def about():
    return """
    <h1>About Me</h1>
    <p>I am a Computer Science student interested in Python and Full Stack Development.</p>
    <a href="{}">Go to Home</a>
    """.format(url_for("home"))


# Dynamic route: subject name and float marks
@app.route("/subject/<string:subject>/<float:marks>")
def subject_marks(subject, marks):
    return f"""
    <h1>Subject Details</h1>
    <p>Subject: {subject}</p>
    <p>Marks: {marks:.2f}</p>
    """


# Dynamic route: generate UUID for a subject
@app.route("/uuid/<string:subject>")
def subject_uuid(subject):
    unique_id = uuid.uuid4()
    return f"""
    <h1>Subject UUID</h1>
    <p>Subject: {subject}</p>
    <p>UUID: {unique_id}</p>
    """


if __name__ == "__main__":
    app.run(debug=True)
