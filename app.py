import sqlite3
from datetime import datetime

# Connect to the database
conn = sqlite3.connect('database/attendance.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll_number TEXT UNIQUE NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    date TEXT,
    status TEXT CHECK(status IN ('Present', 'Absent')),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
)
''')

# Insert a new student
def add_student(name, roll_number):
    try:
        cursor.execute('INSERT INTO students (name, roll_number) VALUES (?, ?)', (name, roll_number))
        conn.commit()
        print(f"Student {name} added successfully.")
    except sqlite3.IntegrityError:
        print(f"Student with roll number {roll_number} already exists.")

# Mark attendance
def mark_attendance(roll_number, status):
    cursor.execute('SELECT student_id FROM students WHERE roll_number = ?', (roll_number,))
    student = cursor.fetchone()
    if student:
        student_id = student[0]
        date = datetime.now().strftime('%Y-%m-%d')
        cursor.execute('INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)', (student_id, date, status))
        conn.commit()
        print(f"Attendance marked for {roll_number} as {status}")
    else:
        print("Student not found!")

# View attendance records
def view_attendance():
    cursor.execute('''
    SELECT s.name, s.roll_number, a.date, a.status
    FROM attendance a
    JOIN students s ON a.student_id = s.student_id
    ORDER BY a.date DESC
    ''')
    records = cursor.fetchall()
    if records:
        print("\nAttendance Records:")
        for record in records:
            print(record)
    else:
        print("No attendance records found.")

# Delete a student
def delete_student(roll_number):
    cursor.execute('DELETE FROM students WHERE roll_number = ?', (roll_number,))
    conn.commit()
    print(f"Student with roll number {roll_number} deleted.")

# Fetch and display all students
def fetch_students():
    cursor.execute('SELECT name, roll_number FROM students')
    students = cursor.fetchall()
    if students:
        print("\nCurrent Students:")
        for student in students:
            print(f"Name: {student[0]}, Roll Number: {student[1]}")
    else:
        print("No students found.")

# Sample operations
def main():
    fetch_students()
    mark_attendance('A101', 'Present')
    mark_attendance('B202', 'Absent')
    print("\nAttendance Records:")
    view_attendance()

if __name__ == "__main__":
    main()

# Close the connection
conn.close()