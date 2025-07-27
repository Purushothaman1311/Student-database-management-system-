# course_manager.py
from db_connector import DBConnector

class CourseManager:
    def __init__(self):
        self.db = DBConnector()
    
    def add_course(self, course_data):
        query = """
        INSERT INTO courses 
        (course_name, course_code, credit_hours, department)
        VALUES (%s, %s, %s, %s)
        """
        conn = self.db.connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, course_data)
                conn.commit()
                return cursor.lastrowid
            except Error as e:
                print(f"Error adding course: {e}")
                return None
            finally:
                self.db.disconnect()
    
    def enroll_student(self, student_id, course_id):
        query = """
        INSERT INTO student_courses 
        (student_id, course_id, enrollment_date)
        VALUES (%s, %s, CURDATE())
        """
        conn = self.db.connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, (student_id, course_id))
                conn.commit()
                return True
            except Error as e:
                print(f"Error enrolling student: {e}")
                return False
            finally:
                self.db.disconnect()
        return False
    
    # Implement other course-related methods
