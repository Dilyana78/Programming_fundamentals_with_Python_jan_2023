items = input().split(", ")
command = input()
while command != "Craft!":
    current_command = command.split(" - ")
    action = current_command[0]

    if action == "Collect":
        item = current_command[1]
        if item not in items:
            items.append(item)
    elif action == 'Drop':
        item = current_command[1]
        if item in items:
            items.remove(item)
    elif action == "Combine":
        item = current_command[2].split(":")
        old_item = item[0]
        new_item = item[1]
        if item in items:
            index_old_item = item.index(old_item)
            index_new_item = index_old_item + 1
            items.insert(index_new_item, new_item)
    elif action == "Renew":
        item = current_command[1]
        if item in items:
            items.remove(item)
            items.append(item)
    command = input()
print(', '.join(items))
