from flask import Flask,render_template,url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/notes")
def notes():
    return render_template("notes.html")


if (__name__ == "__main__"):
    app.run(host='0.0.0.0',
            port=5002,debug=True,use_reloader=False)