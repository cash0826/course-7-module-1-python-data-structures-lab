# This module contains functions to process student data.

def format_student_data(student):
    if student:
        return f"ID: {student[0] } | Name: { student[1] } | Major: { student[2] }"
    return ""
    
def display_students(student_list):
    if student_list:
        for student in student_list:
            data = format_student_data(student)
            print(data)
    else: 
        print("No Students")

    # Display all student records.
    # Loop through the student_list and print each student using format_student_data().