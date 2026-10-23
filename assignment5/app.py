
from flask import Flask

app = Flask(__name__)

# Student records
students = [
    {"id": 1, "name": "Ravi", "percentage": 92},
    {"id": 2, "name": "Sita", "percentage": 85},
    {"id": 3, "name": "Kiran", "percentage": 78},
    {"id": 4, "name": "Priya", "percentage": 65},
    {"id": 5, "name": "Rahul", "percentage": 88},
    {"id": 6, "name": "Anu", "percentage": 55},
    {"id": 7, "name": "Arjun", "percentage": 72},
    {"id": 8, "name": "Sneha", "percentage": 95},
    {"id": 9, "name": "Vijay", "percentage": 35},
    {"id": 10, "name": "Meena", "percentage": 81}
]


@app.route("/")
def home():
    result = """
    <html>
    <head>
        <title>Student Records</title>
    </head>
    <body>
        <h1>Student Records</h1>
        <table border="1" cellpadding="10">
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Percentage</th>
                <th>Grade</th>
            </tr>
    """

    for student in students:
        marks = student["percentage"]

        if marks > 80:
            grade = "A"
        elif marks > 60:
            grade = "B"
        elif marks > 40:
            grade = "C"
        else:
            grade = "Fail"

        result += f"""
            <tr>
                <td>{student['id']}</td>
                <td>{student['name']}</td>
                <td>{marks}%</td>
                <td>{grade}</td>
            </tr>
        """

    result += """
        </table>
    </body>
    </html>
    """

    return result


if __name__ == "__main__":
    app.run(debug=True)
