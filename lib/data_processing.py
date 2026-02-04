# This module contains functions to process student data.

students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]

def format_student_data(student):
    print(f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}")

def display_students(student_list):
    if student_list:
        for student in student_list:
            format_student_data(student)
    else: 
        print("No student list found")

    # Display all student records.
    # Loop through the student_list and print each student using format_student_data().

display_students(students)