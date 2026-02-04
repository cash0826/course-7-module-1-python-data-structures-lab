# This module contains functions for filtering student data.

students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]

def filter_students_by_major(student_list, major):
    filtered_students = [student for student in student_list if student[2].lower() == major.lower()]
    print(filtered_students)
    
    # Defensive (checking for bad input)
    # if filtered_students:
    #     print(f"\nStudents with Major in {major}:")
    #     print(filtered_students)
    # else:
    #     print(f"\nNo Students with Major in {major}")
    
    # Return a filtered list of students by major using a list comprehension.
    # The function should:
    # - Check if a student's major matches the given major (case insensitive).
    # - Return a new list containing only students that match.
    

filter_students_by_major(students, "music")