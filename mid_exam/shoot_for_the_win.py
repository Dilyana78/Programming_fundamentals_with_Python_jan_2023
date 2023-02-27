list_of_targets = [int(target) for target in input().split()]
indices = input()
targets_counter = 0
while indices != "End":
    current_index = int(indices)
    if current_index < len(list_of_targets):
        targets_counter += 1
        value = list_of_targets[current_index]
        list_of_targets[current_index] = -1
        for i in range(len(list_of_targets)):
            if list_of_targets[i] != -1:
                if list_of_targets[i] > value:
                    list_of_targets[i] -= value
                else:
                    list_of_targets[i] += value
    indices = input()

print(f"Shot targets: {targets_counter} -> {' '.join([str(i) for i in list_of_targets])}")