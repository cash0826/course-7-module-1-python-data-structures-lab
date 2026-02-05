from student_data import students
from filters import filter_students_by_major
from data_processing import display_students, format_student_data
from set_operations import unique_majors
from data_generator import student_generator

# print(students)

# print(filter_students_by_major(students, "computer science"))

display_students(students)

majors = unique_majors(students)
print(majors)

print('Students Majors (generator)')
for major_students in student_generator(students, "Physics"):
  print(major_students)