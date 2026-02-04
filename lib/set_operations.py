# This module contains operations related to sets.

students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]

def unique_majors(student_list):
    unique_majors = {student[2] for student in student_list}
    print(unique_majors)
    
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """

unique_majors(students)