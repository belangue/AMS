
from flask import Flask,render_template,redirect, request, url_for
from router.authRouter import auth
from router.studentRouter import student
from router.teacherRouter import teacher
from router.subjectRouter import subject
# from template
app = Flask(__name__)


@app.route("/")
def hello_world():
    name = "John"
    return render_template('login.html', name=name)
    # return "Hello, World Welcome to the result app!"

# Optional URL prefix
# app.register_blueprint(result, url_prefix='/api/result')
app.register_blueprint(auth, url_prefix='/api/auth')
app.register_blueprint(student, url_prefix='/api/student')
app.register_blueprint(teacher, url_prefix='/api/teacher')
app.register_blueprint(subject, url_prefix='/api/subject')

# Mock data for demonstration
students_data = [
    {'id': 1, 'name': 'Alice', 'attendance': {'period1': 'Present', 'period2': 'Absent', 'period3': 'Late', 'period4': 'Present'}},
    {'id': 2, 'name': 'Bob', 'attendance': {'period1': 'Absent', 'period2': 'Present', 'period3': 'Present', 'period4': 'Late'}},
    {'id': 3, 'name': 'Charlie', 'attendance': {'period1': 'Late', 'period2': 'Late', 'period3': 'Absent', 'period4': 'Present'}},
]

@app.route('/attendance', methods=['GET'])
def attendance():
    return render_template('attendance.html', students=students_data)

@app.route('/update_attendance', methods=['POST'])
def update_attendance():
    # Access raw form data
    raw_data = request.form.to_dict()

    # Transform raw data into a structured dictionary
    updated_attendance = {}
    for key, value in raw_data.items():
        if key.startswith('attendance'):
            # Extract student ID and period from the key
            parts = key.split('[')
            student_id = parts[1][:-1]  # Extracts the student ID
            period = parts[2][:-1]     # Extracts the period

            # Initialize student dictionary if not already done
            if student_id not in updated_attendance:
                updated_attendance[student_id] = {}
            
            # Add the period's attendance
            updated_attendance[student_id][period] = value

    # Debugging: Print the structured attendance dictionary
    print(updated_attendance)
    
    return redirect(url_for('attendance'))

if __name__ == "__main__":
    app.run(debug=True)
