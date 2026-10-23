
from flask import Flask, request, url_for, render_template_string

app = Flask(__name__)

# 1. Home page and navigation
@app.route("/")
def home():
    return f"""
        <h1>Home Page</h1>
        <a href="{url_for('about')}">About</a><br>
        <a href="{url_for('signup')}">Signup</a>
    """

@app.route("/about")
def about():
    return "Welcome to About Page"


# 2. GET request: name and batch number
@app.route("/getdata")
def getdata():
    name = request.args.get("name")
    batchno = request.args.get("batchno")
    return f"Name: {name}, Batch No: {batchno}"


# 3. POST request: name and skills using JSON
@app.route("/postdata", methods=["POST"])
def postdata():
    data = request.get_json()
    return f"Name: {data['name']}, Skills: {data['skills']}"


# 4. Signup form
@app.route("/signup")
def signup():
    return render_template_string("""
        <h2>Signup Form</h2>
        <form method="POST" action="/signupdata">
            Username: <input type="text" name="username" required><br><br>
            Email: <input type="email" name="email" required><br><br>
            Address: <input type="text" name="address" required><br><br>
            Password: <input type="password" name="password" required><br><br>
            <button type="submit">Signup</button>
        </form>
    """)


# 5. Collect signup data
@app.route("/signupdata", methods=["POST"])
def signupdata():
    username = request.form.get("username")
    email = request.form.get("email")
    address = request.form.get("address")
    password = request.form.get("password")

    return f"""
        <h2>Signup Successful</h2>
        Username: {username}<br>
        Email: {email}<br>
        Address: {address}<br>
        Password: Received successfully
    """


if __name__ == "__main__":
    app.run(debug=True)
