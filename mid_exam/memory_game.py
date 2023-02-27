str_input = input().split()
command = input()
moves = 0

while command != "end":
    moves += 1
    current_command = command.split()
    index1 = int(current_command[0])
    index2 = int(current_command[1])
    if index1 == index2 or index1 >= len(str_input) or index2 >= len(str_input) or index1 < 0 or index2 < 0:
        str_input.insert(int(len(str_input) / 2), f"-{str(moves)}a")
        str_input.insert(int(len(str_input) / 2), f"-{str(moves)}a")
        print("Invalid input! Adding additional elements to the board")
    elif str_input[index1] == str_input[index2]:
        print(f"Congrats! You have found matching elements - {str_input[index1]}!")
        x = str_input.pop(index1)
        str_input.remove(x)
    elif str_input[index1] != str_input[index2]:
        print("Try again!")
    if len(str_input) == 0:
        print(f"You have won in {moves} turns!")
        exit()
    command = input()
print("Sorry you lose :(")
print(f"{' '.join(str_input)}")
