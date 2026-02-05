# This module contains functions to lazily generate student data.

# Generate next student record filtered by major lazily for memory efficiency
# using a Python generator.

# Args:
#     student_list: List of student tuples (id, name, major)
#     major: Major to filter by (case-insensitive)
    
# Yields:
#     List of Student tuples matching the given major
    
def student_generator(student_list, major):
    
     return (student for student in student_list 
            if student[2].lower() == major.lower())