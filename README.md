# Student-Database-Management-System

pip install mysql-connector-python

CREATE DATABASE IF NOT EXISTS student_management;

USE student_management;

CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    gender ENUM('Male', 'Female', 'Other'),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    enrollment_date DATE,
    major VARCHAR(100),
    current_year INT,
    gpa DECIMAL(3,2)
);

db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'student_management'
}

python student_management.py

import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection"""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='student_management'
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def add_student(student_data):
    """Add a new student to the database"""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = """INSERT INTO students 
                        (first_name, last_name, date_of_birth, gender, 
                         email, phone, address, enrollment_date, major, current_year, gpa)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, student_data)
            conn.commit()
            print("Student added successfully!")
        except Error as e:
            print(f"Error adding student: {e}")
        finally:
            cursor.close()
            conn.close()

# [Additional functions for view, search, update, delete operations]

Security Considerations
Never commit database credentials to version control

Use environment variables for sensitive information

Implement proper input validation to prevent SQL injection

Consider using an ORM (like SQLAlchemy) for production systems

License
This project is open-source and available under the MIT License.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

Support
For any issues or questions, please open an issue in the GitHub repository.
