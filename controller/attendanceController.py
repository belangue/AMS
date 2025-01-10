
from flask import Flask, jsonify, request
from models.attendance import Attendance

def get_all_attendance():
    """
    Fetch all attendance records.
    """
    try:
        return jsonify({"attendance_records": Attendance().read()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def create_attendance():
    """
    Create a new attendance record.
    """
    try:
        data = request.get_json()
        attendance = Attendance(
            sub_code=data["sub_code"],
            student_id=data["student_id"],
            teacher_id=data["teacher_id"],
            date=data["date"],
            hour=data["hour"],
            status=data["status"]
        )
        attendance.save()
        return jsonify({'message': 'Attendance record created successfully', 'att_id': attendance.att_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def update_attendance(att_id):
    """
    Update an existing attendance record.
    """
    try:
        data = request.get_json()
        attendance = Attendance(
            att_id=att_id,
            sub_code=data["sub_code"],
            student_id=data["student_id"],
            teacher_id=data["teacher_id"],
            date=data["date"],
            hour=data["hour"],
            status=data["status"]
        )
        attendance.save()
        return jsonify({'message': 'Attendance record updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def delete_attendance(att_id):
    """
    Delete an attendance record by ID.
    """
    try:
        Attendance().delete(id=att_id)
        return jsonify({'message': f'Attendance record with ID {att_id} deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def update_attendance_status(att_id):
    """
    Update the status of a specific attendance record.
    """
    try:
        data = request.get_json()
        new_status = data["status"]
        Attendance().update_status(att_id=att_id, new_status=new_status)
        return jsonify({'message': f'Attendance status updated to {new_status} for ID {att_id}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
