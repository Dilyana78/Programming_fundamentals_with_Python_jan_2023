def is_index_valid(idx, seq):
    return 0 <= idx < len(seq)

treasure_chest = input().split("|")
command = input()

while command != "Yohoho!":
    current_command = command.split()
    action = current_command[0]
    if action == "Loot":
        lenght = len(current_command)
        items = []
        for i in range(1, lenght):
            items.append(current_command[i])
        for item in items:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)
    elif action == "Drop":
        index = int(current_command[1])
        if is_index_valid(index, treasure_chest):
            item = treasure_chest[index]
            treasure_chest.remove(item)
            treasure_chest.append(item)
    elif action == "Steal":
        stolen_items = []
        count = int(current_command[1])
        if len(treasure_chest) >= count:
            for _ in range(count):
                stealed_items = treasure_chest.pop()
                stolen_items.append(stealed_items)
        else:
            for _ in range(len(treasure_chest)):
                stealed_items = treasure_chest.pop()
                stolen_items.append(stealed_items)
        stolen_items.reverse()
        print(', '.join(stolen_items))
    command = input()

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    items_sum = 0
    for i in treasure_chest:
        items_sum += len(i)
    avg_gain = items_sum / len(treasure_chest)
    print(f"Average treasure gain: {avg_gain:.2f} pirate credits.")
