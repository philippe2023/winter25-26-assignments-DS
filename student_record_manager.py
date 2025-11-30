# Student Record Manager - Assignment 1

class Student:
    def __init__(self, name, student_id, courses_and_grades):
        self.name = name
        self.student_id = student_id

        if isinstance(courses_and_grades, (list, tuple)):
            temp_dict = {}
            for pair in courses_and_grades:
                course = pair[0]
                grade = pair[1]
                temp_dict[course] = grade
            self.courses_and_grades = temp_dict
        else:
            self.courses_and_grades = courses_and_grades

    def get_average_grade(self):
        if len(self.courses_and_grades) == 0:
            return 0

        total = 0
        for grade in self.courses_and_grades.values():
            total += grade

        avg = total / len(self.courses_and_grades)
        return avg

    def add_course_and_grade(self, course_name, grade):
        self.courses_and_grades[course_name] = grade

    def get_honors_courses(self, threshold=90):
        honors_list = []
        for course, grade in self.courses_and_grades.items():
            if grade >= threshold:
                honors_list.append(course)
        return honors_list

    def get_unique_grades(self):
        unique_grades = set()
        for grade in self.courses_and_grades.values():
            unique_grades.add(grade)
        return unique_grades


students = []

# student v1 - dict
student1 = Student(
    name="Jean",
    student_id="STU001",
    courses_and_grades={
        "Math": 82,
        "Science": 91,
        "IT": 85
    }
)

# student v2 - tuple
student2_courses = (
    ("German", 95),
    ("English", 88),
    ("French", 90)
)
student2 = Student(
    name="Sandra",
    student_id="STU002",
    courses_and_grades=student2_courses
)

# Student v3 - dict
student3 = Student(
    name="Max",
    student_id="STU003",
    courses_and_grades={
        "Math": 65,
        "Science": 69,
        "English": 62
    }
)

# student v4 - dict
student4 = Student(
    name="Chris",
    student_id="STU001",
    courses_and_grades={
        "Math": 90,
        "Science": 98,
        "IT": 98
    }
)

students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)

print("STUDENT RECORD MANAGER - RESULTS")

print(f"List of Students: {[student.name for student in students]}")


for student in students:
    average = student.get_average_grade()

    if average > 80:
        honors = student.get_honors_courses()
        print(
            f"{student.name} has an excellent average of {average:.2f} "
            f"and the following honor courses: {honors}"
        )
    else:
        student.add_course_and_grade("Study Skills", 100)
        new_average = student.get_average_grade()
        print(
            f"{student.name} had an average of {average:.2f}, "
            f"so 'Study Skills' with grade 100 was added. "
            f"New average is now {new_average:.2f}."
        )

print("\nUnique grades for each student:")
for student in students:
    print(f"\nStudent: {student.name} (ID: {student.student_id})")
    print(f"{student.name} unique grades: {student.get_unique_grades()}")