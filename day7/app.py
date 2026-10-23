from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    data = 358
    student_details = [
        {'id': 1, 'name': 'sanjay', 'age': 22},
        {'id': 2, 'name': 'rocky', 'age': 23},
        {'id': 3, 'name': 'sanjay rocky', 'age': 24}
    ]
    return render_template('index.html',d = data,p=student_details)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)