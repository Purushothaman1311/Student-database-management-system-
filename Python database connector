# db_connector.py
import mysql.connector
from mysql.connector import Error

class DBConnector:
    def __init__(self):
        self.connection = None
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='student_management',
                user='your_username',
                password='your_password'
            )
            return self.connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None
    
    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
