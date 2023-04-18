student_data = input().split(":")
students = {}
while len(student_data) > 1:
    name, id, course = student_data[0], student_data[1], student_data[2]
    if course not in students.keys():
        students[course] = []
    students[course].append(f"{name} - {id}")
    student_data = input().split(":")
searched_course = student_data[0].replace("_", " ")
for student in students[searched_course]:
    print(student)

# 2 version
student_data = input()
# courses = {}
# while ":" in student_data:
#     student_data = student_data.split(":")
#     student_name, student_id, course = student_data[0], student_data[1], student_data[2]
#     if course not in courses:
#         courses[course] = {}
#     courses[course][student_id] = student_name
#     student_data = input()
# required_course = " ".join(student_data.split("_"))
# for id, name in courses[required_course].items():
#     print(f"{name} - {id}")
