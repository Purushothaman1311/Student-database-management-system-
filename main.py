# main.py
from student_manager import StudentManager
from course_manager import CourseManager

def display_menu():
    print("\n" + "="*50)
    print("Student Database Management System")
    print("="*50)
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Add New Course")
    print("4. Enroll Student in Course")
    print("5. Search Student")
    print("6. Update Student")
    print("7. Delete Student")
    print("8. Generate Reports")
    print("9. Exit")
    print("="*50)

def main():
    student_manager = StudentManager()
    course_manager = CourseManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == '1':  # Add New Student
            print("\n--- Add New Student ---")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            email = input("Email: ")
            phone = input("Phone: ")
            address = input("Address: ")
            
            data = (first_name, last_name, dob, email, phone, address)
            student_id = student_manager.add_student(data)
            
            if student_id:
                print(f"✅ Student added successfully! Student ID: {student_id}")
            else:
                print("❌ Failed to add student.")
                
        elif choice == '2':  # View All Students
            print("\n--- All Students ---")
            students = student_manager.get_all_students()
            if students:
                for student in students:
                    print(student)
            else:
                print("No students found.")
                
        elif choice == '3':  # Add New Course
            print("\n--- Add New Course ---")
            course_name = input("Course Name: ")
            course_code = input("Course Code: ")
            credit_hours = int(input("Credit Hours: "))
            department = input("Department: ")
            
            data = (course_name, course_code, credit_hours, department)
            course_id = course_manager.add_course(data)
            
            if course_id:
                print(f"✅ Course added successfully! Course ID: {course_id}")
            else:
                print("❌ Failed to add course.")
                
        elif choice == '4':  # Enroll Student in Course
            print("\n--- Enroll Student ---")
            try:
                student_id = int(input("Enter Student ID: "))
                course_id = int(input("Enter Course ID: "))
                if course_manager.enroll_student(student_id, course_id):
                    print("✅ Student enrolled successfully!")
                else:
                    print("❌ Enrollment failed.")
            except ValueError:
                print("❌ Please enter valid numbers.")
                
        elif choice == '5':  # Search Student
            print("\n--- Search Student ---")
            search_term = input("Enter name or email to search: ")
            students = student_manager.search_student(search_term)
            if students:
                for student in students:
                    print(student)
            else:
                print("No matching students found.")
                
        elif choice == '6':  # Update Student (You can expand this)
            print("\n--- Update Student ---")
            student_id = int(input("Enter Student ID to update: "))
            # Add more input fields similar to Add Student
            print("Update feature - implement full fields as needed")
            # student_manager.update_student(student_id, new_data)
            
        elif choice == '7':  # Delete Student
            print("\n--- Delete Student ---")
            student_id = int(input("Enter Student ID to delete: "))
            if student_manager.delete_student(student_id):
                print("✅ Student deleted successfully!")
            else:
                print("❌ Failed to delete student.")
                
        elif choice == '8':  # Generate Reports (Basic)
            print("\n--- Reports ---")
            print("1. Total Students:", len(student_manager.get_all_students()))
            # You can expand this later
            
        elif choice == '9':  # Exit
            print("Thank you for using Student Database Management System!")
            break
            
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
