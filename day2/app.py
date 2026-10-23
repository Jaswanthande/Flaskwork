from flask import Flask
#create a Flask application instance
app = Flask(__name__)
#now we will define a route for the root URL ("/") of our application. When a user visits this URL, the function below will be executed and return a response.
@app.route('/')
def hello():
    return "Hello, World!"  
@app.route('/jaswanth')
def details():
    return "My name is Jaswanth, and I am a software developer."
@app.route('/about')
def about():
    return "This is a simple Flask application that demonstrates routing and returning responses."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Run the application on all available network interfaces and port 5000 with debug mode enabled