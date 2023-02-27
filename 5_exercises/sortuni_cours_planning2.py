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