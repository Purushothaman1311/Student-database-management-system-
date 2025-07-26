import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')
conn.commit()

def add_student(name, age, grade):
    cursor.execute('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', (name, age, grade))
    conn.commit()
    print("Student added successfully.")

def display_students():
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    print("\nID\tName\tAge\tGrade")
    print("-"*30)
    for row in rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
    print()

def update_student(student_id, name=None, age=None, grade=None):
    # Build update query dynamically
    updates = []
    params = []
    if name:
        updates.append("name=?")
        params.append(name)
    if age:
        updates.append("age=?")
        params.append(age)
    if grade:
        updates.append("grade=?")
        params.append(grade)
    params.append(student_id)
    query = f"UPDATE students SET {', '.join(updates)} WHERE id=?"
    cursor.execute(query, params)
    conn.commit()
    print("Student record updated.")

def delete_student(student_id):
    cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
    conn.commit()
    print("Student record deleted.")

def menu():
    while True:
        print("\nStudent Database Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            add_student(name, age, grade)
        elif choice == "2":
            display_students()
        elif choice == "3":
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name (leave blank to skip): ")
            age = input("Enter new age (leave blank to skip): ")
            grade = input("Enter new grade (leave blank to skip): ")
            update_student(
                student_id,
                name if name else None,
                int(age) if age else None,
                grade if grade else None,
            )
        elif choice == "4":
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
    conn.close()