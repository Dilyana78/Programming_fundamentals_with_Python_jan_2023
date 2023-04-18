line = input()
points_by_student = {}
submissions_by_language = {}
while line != "exam finished":
    info = line.split("-")
    if info[1] == "banned":
        student_name = info[0]
        points_by_student.pop(student_name)
        line = input()
        continue
    student = info[0]
    language = info[1]
    points = int(info[2])
    if language not in submissions_by_language:
        submissions_by_language[language] = []
    submissions_by_language[language].append(student)
    if student in points_by_student:
        if points > points_by_student[student]:
            points_by_student[student] = points
    else:
        points_by_student[student] = points
    line = input()
print("Results:")
for student, points in points_by_student.items():
    print(f"{student} | {points}")
print("Submissions:")
for language, students in submissions_by_language.items():
    print(f"{language} - {len(students)}")
