def update_student(self, student_id, student_data):
    query = """
    UPDATE students 
    SET first_name=%s, last_name=%s, date_of_birth=%s, 
        email=%s, phone=%s, address=%s
    WHERE student_id = %s
    """
    conn = self.db.connect()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query, (*student_data, student_id))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error updating student: {e}")
            return False
        finally:
            self.db.disconnect()
    return False

def delete_student(self, student_id):
    query = "DELETE FROM students WHERE student_id = %s"
    conn = self.db.connect()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query, (student_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error deleting student: {e}")
            return False
        finally:
            self.db.disconnect()
    return False

def search_student(self, search_term):
    query = """
    SELECT * FROM students 
    WHERE first_name LIKE %s OR last_name LIKE %s OR email LIKE %s
    """
    conn = self.db.connect()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            like_term = f"%{search_term}%"
            cursor.execute(query, (like_term, like_term, like_term))
            return cursor.fetchall()
        except Error as e:
            print(f"Error searching students: {e}")
            return []
        finally:
            self.db.disconnect()
    return []
