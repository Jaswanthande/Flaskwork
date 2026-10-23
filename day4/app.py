from flask import Flask, redirect, render_template, url_for 
import uuid
app = Flask(__name__)
#we will generate UUID using python's built-in uuid module
@app.route('/')
def home():
     return redirect(url_for('indexPage'))
# @app.route('/generate')
# def generate():
#     id = uuid.uuid4().hex
#     print(id)
#     return f'The generated UUID is: {id}'


@app.route('/')
def student():
    return 'Student Routing Application'


@app.route('/student_name/<name>')
def student_name(name):
    return f'Hello, {name}! Your unique session ID is:' 


@app.route('/student_name/<int:student_id>')
def student_id(student_id):
    return f'Hello, Student! Your ID is: {student_id}'


@app.route('/student_name/<uuid:student_id>')
def generate():
    id = uuid.uuid4().hex
    print(id)
    return f'Hello, Student! Your UUID is: {id}'


@app.route('/student_name/<path:student_id>')
def student_path(student_id):
    return f'Hello, Student! Your path is: {student_id}'


@app.route('/student_attendance/<float:student_attendance>')
def student_attendance(student_attendance):
    return f'Hello, Student! Your attendance is: {student_attendance}'


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5001 , debug=True)