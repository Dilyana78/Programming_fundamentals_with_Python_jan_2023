def is_valid_index(idx, seq):
    return 0 <= idx < len(seq)


list_of_coffee = input().split()
n_commands = int(input())
for _ in range(1, n_commands + 1):
    current_command = input().split()
    command = current_command[0]
    if command == "Include":
        new_coffee = current_command[1]
        list_of_coffee.append(new_coffee)
    elif command == "Remove":
        number_of_coffees = int(current_command[2])
        if number_of_coffees > len(list_of_coffee):
            continue
        else:
            if current_command[1] == "first":
                for i in range(number_of_coffees):
                    list_of_coffee.pop(0)
            elif current_command[1] == "last":
                for i in range(number_of_coffees):
                    list_of_coffee.pop()
    elif command == "Prefer":
        index_1 = int(current_command[1])
        index_2 = int(current_command[2])
        if is_valid_index(index_1, list_of_coffee) and is_valid_index(index_2, list_of_coffee):
            list_of_coffee[index_1], list_of_coffee[index_2] = list_of_coffee[index_2], list_of_coffee[index_1]
        else:
            continue
    elif command == "Reverse":
        list_of_coffee.reverse()

print(f"Coffees: ")
print(' '.join(str(item) for item in list_of_coffee))