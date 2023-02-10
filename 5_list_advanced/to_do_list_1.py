command = input()
to_do_list = [0] * 10

while command != "End":
    current_command = command.split("-")
    priority = int(current_command[0]) - 1
    to_do_list[priority] = current_command[1]
    command = input()
to_do = list(filter(lambda x: x != 0, to_do_list))
print(to_do)