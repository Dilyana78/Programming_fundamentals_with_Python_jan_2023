numbers = [int(x) for x in input().split()]
command = input()

while command != "end":
    current_command = command.split()
    action = current_command[0]
    if action == "swap":
        index1 = int(current_command[1])
        index2 = int(current_command[2])
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    elif action == "multiply":
        index1 = int(current_command[1])
        index2 = int(current_command[2])
        numbers[index1] *= numbers[index2]
    elif action == "decrease":
        numbers = [num - 1 for num in numbers]
    command = input()
numbers_as_str = [str(x) for x in numbers]
print(', '.join(numbers_as_str))