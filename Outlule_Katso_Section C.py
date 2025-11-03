# Section C: Introduction of Dictionaries

# Subjects we want to track
subjects = ["Math", "English", "Science"]

# Main dictionary to store all students
# Format: { "Student Name": {"Math": 90, "English": 80, "Science": 70} }
students = {}

def add_student():
    """Add a new student with their grades"""
    first_name = input("\nEnter student's first name: ")
    surname = input("Enter student's surname: ")
    student_name = first_name + " " + surname

    # if student already exists
    if student_name in students:
        print(f"{student_name} already exists.")
        return

    grades = {}
    for subject in subjects:
        mark = -1
        while mark < 0 or mark > 100:
            mark = int(input(f"Enter marks for {student_name} in {subject} (0-100): "))
        grades[subject] = mark

    students[student_name] = grades
    print(f"{student_name} added successfully!")

def update_student():
    """Update existing student grades"""
    student_name = input("Enter the name of the student to update: ")
    if student_name not in students:
        print("Student not found.")
        add_option = input("Would you like to add this student? (yes/no): ").lower()
        if add_option == "yes":
            add_student()
        else:
            print("Returning to main menu...")


    for subject in subjects:
        new_mark = input(f"Enter new mark for {subject} (press Enter to skip): ")
        if new_mark != "":
            students[student_name][subject] = int(new_mark)
    print(f"{student_name}'s record updated successfully!")

def remove_student():
    """Remove a student"""
    student_name = input("Enter the name of the student to remove: ")
    if student_name in students:
        del students[student_name]
        print(f"{student_name} removed successfully!")
    else:
        print("Student not found. Please check the spelling or try again.")

def view_all_students():
    """Display all students with grades and averages"""
    if not students:
        print("No students in the system.")
        return
    print("\n--- All Student Records ---")
    for name, grades in students.items():
        avg = sum(grades.values()) / len(grades)
        print(f"\n{name}")
        for subject, mark in grades.items():
            print(f"  {subject}: {mark}")
        print(f"  Average: {avg:.2f}")

def view_subject_grades():
    """View all students’ grades for one specific subject"""
    subject = input(f"Enter subject to view ({', '.join(subjects)}): ")
    if subject not in subjects:
        print("Invalid subject.")
        return
    print(f"\n--- {subject} Grades ---")
    if not students:
        print("No students in the system.")
        return
    for name, grades in students.items():
        print(f"{name}: {grades[subject]}")

def search_student():
    """Search and display one student's grades and average"""
    name = input("Enter full student name to search: ")
    if name in students:
        grades = students[name]
        avg = sum(grades.values()) / len(grades)
        print(f"\n{name}'s Grades:")
        for subject, mark in grades.items():
            print(f"  {subject}: {mark}")
        print(f"  Average: {avg:.2f}")
    else:
        print("Student not found.")
        add_option = input("Would you like to add this student? (yes/no): ").lower()
        if add_option == "yes":
            add_student()
        else:
            print("Returning to main menu...")

# ---------------- Main Menu ----------------
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Update Student Grades")
    print("3. Remove Student")
    print("4. View All Students")
    print("5. View Subject Grades")
    print("6. Search for a Student")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        view_all_students()
    elif choice == "5":
        view_subject_grades()
    elif choice == "6":
        search_student()
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")


