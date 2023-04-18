count_pair_lines = int(input())
grades_by_students = {}

for _ in range(count_pair_lines):
    student_name = input()
    grade = float(input())
    if student_name not in grades_by_students:
        grades_by_students[student_name] = []
    grades_by_students[student_name].append(grade)
avg_grades = {name: sum(grades) / len(grades) for name, grades in grades_by_students.items() if sum(grades) / len(grades) >= 4.50}
# for student, grades in grades_by_students.items():
#     avg_grade = sum(grades) / len(grades)
#     if avg_grade >= 4.50:
#         print(f"{student} -> {avg_grade:.2f}")
for student, avg_grade in avg_grades.items():
    print(f"{student} -> {avg_grade:.2f}")
