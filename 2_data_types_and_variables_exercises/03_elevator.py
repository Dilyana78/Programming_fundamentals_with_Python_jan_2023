from math import ceil
number_of_people = int(input())
elevator_capacity = int(input())
courses = ceil(number_of_people / elevator_capacity)
print(courses)

# 2_version
# people = int(input())
# capacity = int(input())
# all_people = people
# counter = 0
# while all_people > 0:
#     counter += 1
#     all_people -= capacity
# print(counter)