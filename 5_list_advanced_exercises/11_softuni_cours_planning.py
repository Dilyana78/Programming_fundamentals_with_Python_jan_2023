courses = input().split(", ")
command = input()

while command != "course start":
    current_command = command.split(":")
    action = current_command[0]
    lesson_title = current_command[1]

    if action == "Add":
        if lesson_title not in courses:
            courses.append(lesson_title)
    elif action == "Insert":
        index = int(current_command[2])
        if lesson_title not in courses:
            courses.insert(index, lesson_title)
    elif action == "Remove":
        if lesson_title + '-Exercise' in courses:
            courses.remove(lesson_title + '-Exercise')
        if lesson_title in courses:
            courses.remove(lesson_title)
    elif action == "Swap":
        second_title = current_command[2]
        if lesson_title in courses and second_title in courses:
            firs_index = courses.index(lesson_title)
            second_index = courses.index(second_title)
            courses[firs_index], courses[second_index] = courses[second_index], courses[firs_index]
        if lesson_title + '-Exercise' in courses:
            courses.remove(lesson_title + '-Exercise')
            courses.insert(courses.index(lesson_title) + 1, lesson_title + '-Exercise')
        if second_title + '-Exercise' in courses:
            courses.remove(second_title + '-Exercise')
            courses.insert(courses.index(second_title) + 1, second_title + '-Exercise')
    elif action == "Exercise":
        if lesson_title in courses:
            if f"{lesson_title}-Exercise" not in courses:
                lesson_title_index = courses.index(lesson_title)
                courses.insert(lesson_title_index + 1, f"{lesson_title}-Exercise")
        else:
            courses.append(lesson_title)
            courses.append(f"{lesson_title}-Exercise")
    command = input()
for index, course in enumerate(courses, start=1):
    print(f"{index}.{course}")


# 2 version
# schedule = input().split(', ')
#
#
# def command_add(schedule: list, lessons_tittle: str):
#     for i in schedule:
#         if i + '-Exercise' in schedule:
#             schedule.remove(i + "-Exercise")
#             schedule.insert(schedule.index(i) + 1, i + '-Exercise')
#     if lessons_tittle not in schedule:
#         schedule.append(lessons_tittle)
#     return schedule
#
#
# def command_insert(schedule: list, lessons_tittle: str, index: int):
#     for i in schedule:
#         if i + '-Exercise' in schedule:
#             schedule.remove(i + "-Exercise")
#             schedule.insert(schedule.index(i) + 1, i + '-Exercise')
#     if lessons_tittle not in schedule:
#         schedule.insert(index, lessons_tittle)
#     return schedule
#
#
# def command_remove(schedule: list, lessons_tittle: str):
#     if lessons_tittle in schedule:
#         schedule.remove(lessons_tittle)
#     return schedule
#
#
# def command_swap(schedule: list, lessons_tittle: str, lessons_tittle1: str):
#     for i in schedule:
#         if i + '-Exercise' in schedule:
#             schedule.remove(i + "-Exercise")
#             schedule.insert(schedule.index(i) + 1, i + '-Exercise')
#     if lessons_tittle in schedule and lessons_tittle1 in schedule:
#         index_lessons_tittle = schedule.index(lessons_tittle)
#         index_lessons_tittle1 = schedule.index(lessons_tittle1)
#         schedule[index_lessons_tittle], schedule[index_lessons_tittle1] = \
#             schedule[index_lessons_tittle1], schedule[index_lessons_tittle]
#         return schedule
#
#
# def command_exercise(schedule: list, lessons_tittle: str):
#     if lessons_tittle not in schedule:
#         exercise_word = lessons_tittle + "-Exercise"
#         schedule.append(lessons_tittle)
#         schedule.append(exercise_word)
#     elif lessons_tittle in schedule and lessons_tittle + '-Exercise' not in schedule:
#         schedule.insert(schedule.index(lessons_tittle) + 1, lessons_tittle + '-Exercise')
#
#     return schedule
#
#
# command = input()
#
# while command != "course start":
#     command = command.split(":")
#     if command[0] == 'Swap':
#         command_swap(schedule, command[1], command[2])
#     elif command[0] == "Add":
#         command_add(schedule, command[1])
#     elif command[0] == "Insert":
#         index = int(command[2])
#         command_insert(schedule, command[1], index)
#     elif command[0] == "Remove":
#         command_remove(schedule, command[1])
#     elif command[0] == "Exercise":
#         command_exercise(schedule, command[1])
#     command = input()
#
# for i, v in enumerate(schedule):
#     print(f'{i + 1}.{v}')