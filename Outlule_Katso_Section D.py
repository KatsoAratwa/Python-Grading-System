# Section D: Modularization with Functions

# Subjects to track
subjects = ["Math", "English", "Science"]

# Main dictionary to store all students
# Format: { "Student Name": {"Math": 90, "English": 80, "Science": 70} }
students = {}

# ---------------- Helper Functions ----------------
def get_average(grades):
    """Calculate and return average marks"""
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)

def display_student(name, grades):
    """Display one student's grades and average"""
    avg = get_average(grades)
    print(f"\n{name}'s Grades:")
    for subject, mark in grades.items():
        print(f"  {subject}: {mark}")
    print(f"  Average: {avg:.2f}")

# ---------------- Core Functions ----------------
def add_student():
    """Add a new student with their grades"""
    try:
        first_name = input("\nEnter student's first name: ").strip()
        surname = input("Enter student's surname: ").strip()
        student_name = first_name + " " + surname

        if student_name in students:
            print(f"{student_name} already exists.")
            return

        grades = {}
        for subject in subjects:
            while True:
                try:
                    mark = int(input(f"Enter marks for {student_name} in {subject} (0–100): "))
                    if 0 <= mark <= 100:
                        grades[subject] = mark
                        break
                    else:
                        print("Please enter a mark between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        students[student_name] = grades
        print(f"{student_name} added successfully!")

    except Exception as e:
        print(f"Error adding student: {e}")

def search_student():
    """Search for a student by name and display their grades"""
    try:
        name = input("Enter full student name to search: ").strip()
        if name in students:
            display_student(name, students[name])
        else:
            print("Student not found.")
            add_option = input("Would you like to add this student? (yes/no): ").lower()
            if add_option == "yes":
                add_student()
    except Exception as e:
        print(f"Error searching for student: {e}")

def update_student():
    """Update existing student grades"""
    try:
        student_name = input("Enter the name of the student to update: ").strip()
        if student_name not in students:
            print("Student not found.")
            add_option = input("Would you like to add this student? (yes/no): ").lower()
            if add_option == "yes":
                add_student()
            return

        for subject in subjects:
            new_mark = input(f"Enter new mark for {subject} (press Enter to skip): ").strip()
            if new_mark:
                try:
                    new_mark = int(new_mark)
                    if 0 <= new_mark <= 100:
                        students[student_name][subject] = new_mark
                    else:
                        print("Invalid mark. Skipped update for this subject.")
                except ValueError:
                    print("Invalid input. Skipped update for this subject.")
        print(f"{student_name}'s record updated successfully!")

    except Exception as e:
        print(f"Error updating student: {e}")

def remove_student():
    """Remove a student"""
    try:
        student_name = input("Enter the name of the student to remove: ").strip()
        if student_name in students:
            del students[student_name]
            print(f"{student_name} removed successfully!")
        else:
            print("Student not found.")
    except Exception as e:
        print(f"Error removing student: {e}")

def view_all_students():
    """Display all students with grades and averages"""
    try:
        if not students:
            print("No students in the system.")
            return

        print("\n--- All Student Records ---")
        for name, grades in students.items():
            display_student(name, grades)
    except Exception as e:
        print(f"Error displaying students: {e}")

def view_subject_grades():
    """View all students’ grades for one specific subject"""
    try:
        subject = input(f"Enter subject to view ({', '.join(subjects)}): ").strip()
        if subject not in subjects:
            print("Invalid subject.")
            return

        print(f"\n--- {subject} Grades ---")
        if not students:
            print("No students in the system.")
            return
        for name, grades in students.items():
            print(f"{name}: {grades[subject]}")
    except Exception as e:
        print(f"Error viewing subject grades: {e}")

# ---------------- Main Menu ----------------
def main_menu():
    """Main control flow for the Student Management System"""
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Update Student Grades")
        print("3. Remove Student")
        print("4. View All Students")
        print("5. View Subject Grades")
        print("6. Search for a Student")
        print("7. Exit")

        choice = input("Choose an option (1–7): ").strip()

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

# Run the system
main_menu()
