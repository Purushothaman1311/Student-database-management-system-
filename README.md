# Student Database Management System (Python & MySQL)

A simple Student Database Management System (SDMS) built using Python and MySQL. This project allows users to perform CRUD (Create, Read, Update, Delete) operations on student records. It demonstrates integration between Python and MySQL for data storage and retrieval.

## Features

- Add new student records
- Display all student records
- Search student by ID or Name
- Update student details
- Delete student records
- Simple command-line interface

## Technologies Used

- **Python 3.x**: Backend logic and CLI
- **MySQL**: Database for storing student information
- **mysql-connector-python**: Python library to connect to MySQL

## Setup Instructions

### 1. Prerequisites

- Python 3 installed on your system
- MySQL server running locally or remotely
- `mysql-connector-python` library installed  
  Install with:
  ```bash
  pip install mysql-connector-python
  ```

### 2. MySQL Database Setup

1. **Create Database and Table**

   ```sql
   CREATE DATABASE student_db;
   USE student_db;

   CREATE TABLE students (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       age INT NOT NULL,
       gender VARCHAR(10),
       email VARCHAR(100)
   );
   ```

2. Note your MySQL username, password, host, and database name for configuring the Python script.

### 3. Clone the Repository

```bash
git clone https://github.com/yourusername/student-dbms-python.git
cd student-dbms-python
```

### 4. Configure Database Connection

Edit the Python script (`main.py` or `student_dbms.py`) and update the following credentials:

```python
db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="student_db"
)
```

### 5. Run the Application

```bash
python student_dbms.py
```

## Example Usage

```
===== Student Database Management System =====
1. Add Student
2. Display All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

Enter your choice: 
```

## File Structure

```
student-dbms-python/
│
├── student_dbms.py     # Main Python script
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

## Contributing

Feel free to fork this repository and submit pull requests.

## License

This project is licensed under the MIT License.

## Author

- [Purushothaman](https://github.com/purushothaman1311)
