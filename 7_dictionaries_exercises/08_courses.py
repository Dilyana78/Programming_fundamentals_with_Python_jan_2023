students_by_courses = {}
command = input()
while command != "end":
    courses = command.split(" : ")
    course_name = courses[0]
    student_name = courses[1]
    if course_name not in students_by_courses:
        students_by_courses[course_name] = []
        students_by_courses[course_name].append(student_name)
    else:
        students_by_courses[course_name].append(student_name)
    command = input()
for course, students in students_by_courses.items():
    print(f"{course}: {len(students)}")

    for student in students:
        print(f"-- {student}")