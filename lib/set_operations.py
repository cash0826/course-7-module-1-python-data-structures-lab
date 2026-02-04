# This module contains operations related to sets.

secondary_students = [
    (101, "Miles", "Mathematics"),
    (102, "Laura", "Mathematics"),
    (103, "Benji", "Physics"),
    (104, "Natalia", "Physics"),
    (105, "Nadia", "Mathematics"),
]

def unique_majors(student_list):
    unique_majors = {student[2] for student in student_list}
    print(unique_majors)
    
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """

unique_majors(secondary_students)