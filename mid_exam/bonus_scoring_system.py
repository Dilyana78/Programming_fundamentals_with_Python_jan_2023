from math import ceil
students = int(input())
lectures = int(input())
bonus = int(input())
max_bonus = 0
max_lectures = 0
for student in range(1, students + 1):
    attendance = int(input())
    total_bonus = (attendance / lectures) * (5 + bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_lectures = attendance
print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_lectures} lectures.")