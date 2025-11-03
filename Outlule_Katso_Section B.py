# Section B: Expanding with Lists and Tuples

# Subjects we want to track
subjects = ["Math", "English", "Science"]

num_students = int(input("How many students?: "))

# Store student records as a list of tuples (name, [grades])
students = []

for _ in range(num_students):
    first_name = input("\nEnter student's first name: ")
    surname = input("Enter student's surname: ")
    student_name = first_name + " " + surname

    grades = []  # list to hold subject grades
    for subject in subjects:
        mark = -1
        while mark < 0 or mark > 100:  # input validation
            mark = int(input(f"Enter marks for {student_name} in {subject} (0-100): "))
        grades.append(mark)

    # store as tuple (name, list_of_grades)
    students.append((student_name, grades))

# --- Enhanced Output ---
print("\n--- Student Summary ---")
for student in students:
    name, grades = student
    avg_grade = sum(grades) / len(grades)
    print(f"\n{name}")
    for i in range(len(subjects)):
        print(f"  {subjects[i]}: {grades[i]}")
    print(f"  Average Grade: {avg_grade:.2f}")

# --- Highest and Lowest per subject ---
print("\n--- Subject Statistics ---")
for i in range(len(subjects)):
    subject_grades = [student[1][i] for student in students]  # extract i-th subject grade from each student
    highest = max(subject_grades)
    lowest = min(subject_grades)
    print(f"{subjects[i]} - Highest: {highest}, Lowest: {lowest}")
