def is_valid_index(idx, seq):
    return 0 <= idx < len(seq)


targets = [int(x) for x in input().split()]
command = input()
int_lenght = len(targets)
while command != "End":
    current_command = command.split()
    action = current_command[0]
    index = int(current_command[1])
    value = int(current_command[2])
    if action == "Shoot":
        if is_valid_index(index, targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])
    elif action == "Add":
        if is_valid_index(index, targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        before_radius = index - value
        after_radius = index + value
        if is_valid_index(after_radius, targets) and is_valid_index(before_radius, targets):
            targets = targets[0:before_radius] + targets[after_radius + 1::]
        else:
            print('Strike missed!')
    command = input()
print('|'.join(str(x) for x in targets))
