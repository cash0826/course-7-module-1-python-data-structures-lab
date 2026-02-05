# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    if student_list:
        # filtered_students = []
        # for student in student_list:
        #     if(student[2].lower() == major.lower()):
        #         filtered_students.append(student)
        # return filtered_students
        return [ student for student in student_list if student[2].lower() == major.lower()]
    
    return []
            
    # filtered_students = [student for student in student_list if student[2].lower() == major.lower()]
    # print(filtered_students)
    
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
    