from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return f'Welcome to Day 3 learning about static vs dyanmic routes in Flask!'
@app.route('/name')
def get_name():
    return 'Jaswanth'

@app.route('/courses')       # Static route
@app.route('/course')        # Static route
def get_course_static():
    return 'Python Full Stack with GENAI'
@app.route('/course/<course_name>')
def get_course(course_name):
    return f'<b>Hello {course_name}, this is your first dynamic route in Flask!</b>'

@app.route('/student/<uuid:student_id>') #dynamic route with integer type
def get_student(student_id):
    return f'Hello Student with ID: {student_id}, this is your first dynamic route in Flask!'

@app.route('/percent/<float:percentage>') #dynamic route with float type
def get_percentage(percentage):
    return f'Hello Student with Percentage: {percentage}, this is your first dynamic route in Flask!'

@app.route('/path/<path:subpath>') #dynamic route with path type
def get_subpath(subpath):
    return f'Hello Student with Subpath: {subpath}, this is your first dynamic route in Flask!'




@app.route('/name/jaswanth') #static route
def get_name_jaswanth():
    return 'Hello Jaswanth this is your first dynamic route in Flask!'
@app.route('/name/<name>') #dyanamic route
def get_name_dynamic(name):
    return f'Hello {name} this is your first dynamic route in Flask!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)