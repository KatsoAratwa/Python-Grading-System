# Python-Grading-System
I was tasked with craeting a grading system that kept being developed over the weeks. I took 7 weeks to create it. This system managed a variety on tasks through the use of sections. My code is simple to understand and the program itself is user frriendly.  

This is what each section is able to do:
Section A
1. It asks students to enter their Names, Surname and their marks out of 100. (I used a loop to handle multiple students)
2. It represents the marks that each student got in te form of a Grade  
3. It creates a Class summary that shows the total number of students, how many failed or passed and gives a class average.

Section B
1. It enters the marks of a student from different subjects that are Math, English and Science
2. It stores the grades in a list and combines the student's name using a tuple.
3. It calculates and displays the average of each student.
4. It creates a Subject statistic that shows the highest and lowest grade for each subject.

Section C
1. It uses dictionaries as the key: values being Student:Grades
2. It displays a main menu that uses functions to add,update,remove, view and search for students.
3. The add_student function is the most important. If you want to update,view or search for a student they have to be added into the program first. I created a loop that prompts a user to add a student first if they are not in the program yet.

Section D
1. It modularized the functions
2. Each function uses the try-except blocks to catch invalid inputs and displays clear messages.

Section F

Section E
1. It has 2 classes called Student and Gradebook that reaplace the global dictionaries and functions used in the previous sections.
2. There is a new function that sorts students. It sorts students by average(highest to lowest), name(alphabetical order) and by subject(highest to lowest in every subject).

Section F
1. The error handling is very comprehensive giving out results like StudentNotFound and InvalidGrade.
2. TESTING SUMMARY:
The entire grading system has been thoroughly tested across all sections (A-F)
to ensure robust operation under various scenarios and edge cases.

TESTING PHASES CONDUCTED:
1. Unit Testing - Individual component testing
2. Integration Testing - Component interaction testing
3. System Testing - End-to-end workflow testing
4. Edge Case Testing - Boundary condition testing
5. Error Handling Testing - Exception scenario testing

SPECIFIC TEST SCENARIOS EXECUTED:
SECTION A & B TESTING:
- Input validation for student counts (negative, zero, large numbers)
- Grade boundary testing (0, 100, -1, 101, non-numeric inputs)
- Empty name handling
- Single student vs multiple students
- Grade calculations accuracy (averages, totals)

SECTION C & D TESTING:
- Dictionary operations (add, update, remove, search)
- Function modularity and parameter passing
- Menu system navigation and error recovery
- Data persistence across operations
- Invalid menu choices handling

SECTION E & F TESTING:
- Class instantiation and method calls
- Inheritance and polymorphism (where applicable)
- Custom exception handling
- Sorting algorithm correctness
- Search functionality (exact, partial, threshold-based)

EDGE CASES TESTED:
1. Empty system operations (no students)
2. Single student operations
3. Maximum grade values (0, 100)
4. Invalid input types (strings instead of numbers)
5. Duplicate student names
6. Case sensitivity in searches
7. Empty string inputs
8. Very large student lists (performance)

ISSUES ENCOUNTERED AND RESOLUTIONS:
1. ISSUE: Duplicate student names allowed in initial implementation
   RESOLUTION: Added duplicate checking in add_student() function

2. ISSUE: Case sensitivity caused search failures
   RESOLUTION: Implemented case-insensitive comparison using .lower()

3. ISSUE: Sorting algorithms modified original lists
   RESOLUTION: Implemented sorting on list copies to preserve original order

4. ISSUE: No validation for empty names
   RESOLUTION: Added EmptyNameError custom exception and validation

5. ISSUE: Grade validation inconsistent across functions
   RESOLUTION: Centralized validation in Student.add_grade() method

6. ISSUE: Error messages not user-friendly
   RESOLUTION: Enhanced exception messages with clear guidance

TESTING RESULTS:
- All core functionalities operational
- Error handling robust and informative
- Sorting algorithms produce correct results
- Search functionality works as expected
- System handles edge cases gracefully
- Code meets all assignment requirements
- 
FINAL VERIFICATION:
The system has been verified to handle:
- Normal operational workflows
- Error conditions and invalid inputs
- Boundary conditions and edge cases
- Performance with realistic data volumes


   
