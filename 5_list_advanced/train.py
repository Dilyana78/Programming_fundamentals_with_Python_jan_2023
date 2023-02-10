number_of_wagons = int(input())
wagons = [0] * number_of_wagons
command = input()

while command != "End":
    current_command = command.split()
    action = current_command[0]
    if action == "add":
        wagons[-1] += int(current_command[1])
    elif action == "insert":
        index = int(current_command[1])
        wagons[index] += int(current_command[2])
    elif action == "leave":
        index = int(current_command[1])
        wagons[index] -= int(current_command[2])
    command = input()
print(wagons)