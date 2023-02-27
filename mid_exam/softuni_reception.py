students_per_hour_efficiency = int(input()) + int(input()) + int(input())
all_students = int(input())
answered_students = 0
hours = 0
while all_students != 0:
    hours += 1
    if all_students < students_per_hour_efficiency:
        answered_students = all_students
    else:
        answered_students = students_per_hour_efficiency
    all_students -= answered_students
    if hours % 4 == 0:
        all_students += answered_students

print(f"Time needed: {hours}h.")
