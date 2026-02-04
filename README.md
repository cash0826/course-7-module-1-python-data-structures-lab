# Student Data Management System Lab

## Setup Instructions

### Install Dependencies

Ensure **Python** is installed:
```sh
python --version
```

Run the following command to install dependencies:
```sh
pipenv install
```

Run the following to enter the virtual environment:
```sh
pipenv shell
```

To run the test suite, use:
```sh
pytest -x
```

## Features

The **Student Data Management System** will be built using structured data handling techniques, including:

- **Lists & Tuples**: Store student data in structured collections.
- **List Comprehensions & Generator Expressions**: Process and filter student records efficiently.
- **Sets**: Track unique student data attributes such as completed courses and enrolled majors.

#### Design Breakdown:
- **Student list storage** using **tuples** and **lists**.
- **Filtering capabilities** using **list comprehensions**.
- **Memory-efficient data handling** with **generator expressions**.
- **Tracking unique attributes** using **sets**.

This structured approach ensures an **efficient, maintainable, and scalable** student data system.

---


### 1: Student Records using Lists and Tuples

In `student_data.py`, student records is defined as a list of students each as tuples.


#### 2: Filtering Students Using List Comprehensions

In `filter.py`, the `filter_students_by_major` function returns a filtered list of students given a major, using a list comprehension.

#### 3: Displaying Student Data

In `data_processing.py`, the `format_student_data` function returns a string for a given student formatted like:
```python
"ID: 10 | Name: Louis Medina | Major: Computer Science"
```

#### 4: Displaying All Students' Data

Also in `data_processing.py`, the `display_students` function loops through all students and print each student's
details using the `format_student_data` function.

#### Step 5: Updating Student Courses Using Set Operations

In `set_operations.py`, the `unique_majors` function returns a set of unique student majors using set comprehension. For example, given a list of students like:
```python
[
    (101, "Miles", "Mathematics"),
    (102, "Laura", "Mathematics"),
    (103, "Benji", "Physics"),
    (104, "Natalia", "Physics"),
    (105, "Nadia", "Mathematics"),
]
```
the `unique_majors` function should return (in no particular order):
```python
{"Mathematics", "Physics"}
```

#### Step 6: Create a Student List Generator by Major

In `data_generator.py`, the `student_generator` function returns a generator expression
for all students by major. Example of a generator expression:

```python
(item_to_return for item_in_iterable in iterable if condition)

# more concrete example:
number_list = [1,2,3,4,5,6]
generator_expression = (n * 2 for n in number_list if n > 3)
```
---

## Best Practices for Managing Student Data

- **Use comments** to clarify logic.
- **Optimize lookups** with dictionary `.get()` method.
- **Use set operations** for efficient course tracking.
- **Apply generator expressions** for memory efficiency.
- **Update README** to document functionality.

## Conclusion

By mastering **Sequences, List Comprehensions, Generator Expressions, Dictionaries, and Sets**, developers can:

- Optimize **student data storage and retrieval**.
- Enhance **performance using efficient data structures**.
- Improve **scalability using structured data management techniques**.

This lab ensures real-world applicability of Python **data structures** in managing dynamic, scalable, and efficient datasets.