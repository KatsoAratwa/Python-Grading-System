#Section A
#Student Data Entry
num_students = int(input("How many students?: "))

# Counters
passed = 0
failed = 0
total_marks = 0  # for average calculation

for student in range(num_students):
    first_name = input("\nEnter student name: ")
    surname = input("Enter student's surname: ")
    student_name = first_name + " " + surname #join them with a space

    # Input Validation
    marks = -1
    while marks < 0 or marks > 100:
        marks = int(input(f"Enter marks for {student_name} (0-100): "))

    # Letter Grade Classification
    if 90 <= marks <= 100:
        grade = "A*"
    elif 80 <= marks <= 89:
        grade = "A"
    elif 70 <= marks <= 79:
        grade = "B"
    elif 60 <= marks <= 69:
        grade = "C"
    elif 50 <= marks <= 59:
        grade = "D"
    elif 40 <= marks <= 49:
        grade = "E"
    else:
        grade = "U (Fail)"

    # Distinction/Pass/Fail Classification
    if marks >= 70:
        result = "Distinction"
        passed += 1
    elif marks >= 50:
        result = "Pass"
        passed += 1
    else:
        result = "Fail"
        failed += 1

    # Add marks to total
    total_marks += marks

    # Print result for this student
    print(f"{student_name}: {marks} --- Grade: {grade}, Result: {result}")

# Final Class Stats
average= total_marks / num_students
print("\n--- Class Summary ---")
print(f"Total Students: {num_students}")
print(f"Passed: {passed}, Failed: {failed}")
print(f"Class Average: {average:.2f}")
