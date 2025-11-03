# Section E: Transition to Object-Oriented Programming (OOP)

class Student:
    """Represents a student with their grades"""

    def __init__(self, first_name, surname):
        self.first_name = first_name
        self.surname = surname
        self.grades = {}  # Dictionary to store subject: grade pairs

    @property
    def full_name(self):
        return f"{self.first_name} {self.surname}"

    def add_grade(self, subject, grade):
        """Add or update a grade for a subject"""
        self.grades[subject] = grade

    def get_average(self):
        """Calculate and return the average grade"""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def display_info(self):
        """Display student's information and grades"""
        print(f"\n{self.full_name}")
        for subject, grade in self.grades.items():
            print(f"  {subject}: {grade}")
        print(f"  Average: {self.get_average():.2f}")


class Gradebook:
    """Manages a collection of Student objects"""

    def __init__(self):
        self.students = []  # List to store Student objects
        self.subjects = ["Math", "English", "Science"]

    def add_student(self, student):
        """Add a student to the gradebook"""
        self.students.append(student)
        print(f"Student {student.full_name} added successfully!")

    def remove_student(self, full_name):
        """Remove a student by full name"""
        for i, student in enumerate(self.students):
            if student.full_name.lower() == full_name.lower():
                removed_student = self.students.pop(i)
                print(f"Student {removed_student.full_name} removed successfully!")
                return True
        print("Student not found.")
        return False

    def search_student(self, full_name):
        """Search for a student by name"""
        for student in self.students:
            if student.full_name.lower() == full_name.lower():
                return student
        return None

    def display_all_students(self):
        """Display all students in the gradebook"""
        if not self.students:
            print("No students in the system.")
            return

        print("\n--- All Student Records ---")
        for student in self.students:
            student.display_info()

    def display_subject_grades(self, subject):
        """Display all students' grades for a specific subject"""
        if subject not in self.subjects:
            print("Invalid subject.")
            return

        print(f"\n--- {subject} Grades ---")
        if not self.students:
            print("No students in the system.")
            return

        for student in self.students:
            grade = student.grades.get(subject, "No grade")
            print(f"{student.full_name}: {grade}")

    def sort_students_by_average(self, descending=True):
        """Sort students by their average grade"""
        return sorted(self.students,
                      key=lambda student: student.get_average(),
                      reverse=descending)

    def sort_students_by_name(self):
        """Sort students alphabetically by name"""
        return sorted(self.students, key=lambda student: student.full_name)

    def sort_students_by_subject(self, subject):
        """Sort students by grade in a specific subject"""
        if subject not in self.subjects:
            print("Invalid subject.")
            return self.students

        return sorted(self.students,
                      key=lambda student: student.grades.get(subject, 0),
                      reverse=True)


def add_student(gradebook):
    """Add multiple students to the gradebook"""
    try:
        # Ask how many students to add
        num_students = int(input("\nHow many students do you want to add? "))

        if num_students <= 0:
            print("Please enter a positive number.")
            return

        students_added = 0

        for i in range(num_students):
            print(f"\n--- Adding Student {i + 1} of {num_students} ---")

            first_name = input("Enter student's first name: ").strip()
            if not first_name:
                print("First name cannot be empty. Skipping this student.")
                continue

            surname = input("Enter student's surname: ").strip()
            if not surname:
                print("Surname cannot be empty. Skipping this student.")
                continue

            # Check if student already exists
            full_name = f"{first_name} {surname}"
            if gradebook.search_student(full_name):
                print(f"Student {full_name} already exists. Skipping...")
                continue

            student = Student(first_name, surname)

            # Add grades for each subject
            for subject in gradebook.subjects:
                while True:
                    try:
                        mark_input = input(f"Enter marks for {subject} (0-100): ").strip()
                        if not mark_input:
                            print(f"Skipping {subject}...")
                            break

                        mark = int(mark_input)
                        if mark < 0 or mark > 100:
                            print("Grade must be between 0 and 100.")
                            continue

                        student.add_grade(subject, mark)
                        break

                    except ValueError:
                        print("Invalid input. Please enter a number.")

            gradebook.add_student(student)
            students_added += 1

        print(f"\nSuccessfully added {students_added} student(s) to the system.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"Error adding students: {e}")


def main_oop_system():
    """Main function to run the OOP-based grading system"""
    gradebook = Gradebook()

    while True:
        print("\n" + "=" * 50)
        print("        STUDENT GRADING SYSTEM (OOP)")
        print("=" * 50)
        print("1. Add Student(s)")
        print("2. Update Student Grades")
        print("3. Remove Student")
        print("4. View All Students")
        print("5. View Subject Grades")
        print("6. Search for a Student")
        print("7. Sort Students (by average)")
        print("8. Sort Students (by name)")
        print("9. Sort Students (by subject)")
        print("10. Exit")
        print("=" * 50)

        choice = input("Choose an option (1-10): ").strip()

        try:
            if choice == "1":
                add_student(gradebook)

            elif choice == "2":
                name = input("Enter student name to update: ").strip()
                student = gradebook.search_student(name)
                if student:
                    print(f"Updating grades for {student.full_name}:")
                    for subject in gradebook.subjects:
                        new_grade = input(f"Enter new grade for {subject} (press Enter to skip): ").strip()
                        if new_grade:
                            try:
                                grade = int(new_grade)
                                if 0 <= grade <= 100:
                                    student.add_grade(subject, grade)
                                else:
                                    print("Invalid grade. Must be between 0-100.")
                            except ValueError:
                                print("Invalid input. Please enter a number.")
                    print("Grades updated successfully!")
                else:
                    print("Student not found.")

            elif choice == "3":
                name = input("Enter student name to remove: ").strip()
                gradebook.remove_student(name)

            elif choice == "4":
                gradebook.display_all_students()

            elif choice == "5":
                subject = input(f"Enter subject ({', '.join(gradebook.subjects)}): ").strip()
                gradebook.display_subject_grades(subject)

            elif choice == "6":
                name = input("Enter student name to search: ").strip()
                student = gradebook.search_student(name)
                if student:
                    student.display_info()
                else:
                    print("Student not found.")

            elif choice == "7":
                sorted_students = gradebook.sort_students_by_average()
                print("\n--- Students Sorted by Average Grade (Highest First) ---")
                for student in sorted_students:
                    print(f"{student.full_name}: {student.get_average():.2f}")

            elif choice == "8":
                sorted_students = gradebook.sort_students_by_name()
                print("\n--- Students Sorted by Name ---")
                for student in sorted_students:
                    print(f"{student.full_name}: {student.get_average():.2f}")

            elif choice == "9":
                subject = input(f"Enter subject to sort by ({', '.join(gradebook.subjects)}): ").strip()
                sorted_students = gradebook.sort_students_by_subject(subject)
                if sorted_students:
                    print(f"\n--- Students Sorted by {subject} Grade ---")
                    for student in sorted_students:
                        grade = student.grades.get(subject, "No grade")
                        print(f"{student.full_name}: {grade}")

            elif choice == "10":
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")


# Run the OOP system
if __name__ == "__main__":
    main_oop_system()