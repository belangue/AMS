# test.py
from app import app, db, Teacher, Student, Attendance

with app.app_context():
    try:
        # Try to create the database
        db.create_all()
        print("Database created successfully!")
        
        # Try to query existing data
        teachers = Teacher.query.all()
        students = Student.query.all()
        
        print(f"\nFound {len(teachers)} teachers")
        print(f"Found {len(students)} students")
        
    except Exception as e:
        print("Error:", str(e))