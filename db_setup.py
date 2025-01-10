from app import app, db, Teacher, Student, Attendance
from werkzeug.security import generate_password_hash
from datetime import datetime
import os

def setup_database():
    
    print(f"Current working directory: {os.getcwd()}")
    
    with app.app_context():
        try:
            print("Dropping existing tables...")
            db.drop_all()
            print("✓ Existing tables dropped")
            
            print("Creating new tables...")
            db.create_all()
            print("✓ New tables created")
            
            print("Adding test teacher...")
            test_teacher = Teacher(
                name='Test Teacher',
                subject='Mathematics',
                password=generate_password_hash('password123')
            )
            db.session.add(test_teacher)
            db.session.commit()
            print("✓ Test teacher added")
            
            print("Adding test students...")
            students = [
                Student(name='Student 1', class_name='10A'),
                Student(name='Student 2', class_name='10A'),
                Student(name='Student 3', class_name='10B')
            ]
            db.session.add_all(students)
            db.session.commit()
            print("✓ Test students added")
            
            print("\nDatabase setup completed successfully!")
            print("\nYou can now log in with:")
            print("Username: Test Teacher")
            print("Password: password123")
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    setup_database()