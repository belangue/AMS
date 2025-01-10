# from base_model import AbstractBaseModel
from config.DataSource import DataSource


class Attendance:
    TABLE_NAME = "attendance"

    def __init__(self, att_id=None, sub_code=None, student_id=None, teacher_id=None, date=None, hour=None, status=None):
        self.att_id = att_id
        self.sub_code = sub_code
        self.student_id = student_id
        self.teacher_id = teacher_id
        self.date = date
        self.hour = hour
        self.status = status
        self.ds = DataSource()

    def save(self):
        # Update attendance record if `att_id` exists; otherwise, insert a new record
        if self.att_id:
            query = f"""
                UPDATE {self.__class__.TABLE_NAME}
                SET sub_code=%s, student_id=%s, teacher_id=%s, date=%s, hour=%s, status=%s
                WHERE att_id=%s
            """
            self.ds.execute(query, (self.sub_code, self.student_id, self.teacher_id, self.date, self.hour, self.status, self.att_id))
        else:
            query = f"""
                INSERT INTO {self.__class__.TABLE_NAME}
                (sub_code, student_id, teacher_id, date, hour, status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.ds.execute(query, (self.sub_code, self.student_id, self.teacher_id, self.date, self.hour, self.status))
            results = self.ds.execute(f"SELECT MAX(att_id) FROM {self.__class__.TABLE_NAME}")
            for result in results:
                self.att_id = result[0]

    def read(self, att_id=None):
        if att_id:
            query = f"SELECT * FROM {self.__class__.TABLE_NAME} WHERE att_id=%s"
            result = self.ds.execute(query, (att_id,))
            return result
        else:
            query = f"SELECT * FROM {self.__class__.TABLE_NAME}"
            results = self.ds.execute(query)
            return results

    def delete(self, att_id=None):
        if att_id:
            query = f"DELETE FROM {self.__class__.TABLE_NAME} WHERE att_id=%s"
            self.ds.execute(query, (att_id,))
            print(f"Attendance record with ID {att_id} deleted successfully.")
        else:
            query = f"DELETE FROM {self.__class__.TABLE_NAME}"
            self.ds.execute(query)
            print("All attendance records deleted successfully.")


    def update_status(self, att_id, new_status):
        # Update the status of a specific attendance record
        query = f"""
            UPDATE {self.__class__.TABLE_NAME}
            SET status=%s
            WHERE att_id=%s
        """
        self.ds.execute(query, (new_status, att_id))
        print(f"Attendance status updated successfully for ID {att_id}.")