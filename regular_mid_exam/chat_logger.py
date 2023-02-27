messages = []


while True:
    current_command = input().split()
    command = current_command[0]
    if command == "end":
        break
    elif command == "Chat":
        message = current_command[1]
        messages.append(message)
    elif command == "Delete":
        message = current_command[1]
        if message in messages:
            messages.remove(message)
        else:
            continue
    elif command == "Edit":
        old_message = current_command[1]
        new_message = current_command[2]
        if old_message in messages:
            index_old = messages.index(old_message)
            messages[index_old] = new_message
        else:
            continue
    elif command == "Pin":
        message = current_command[1]
        if message in messages:
            messages.remove(message)
            messages.append(message)
        else:
            continue
    elif command == "Spam":
        for i in range(1, len(current_command)):
            message = current_command[i]
            messages.append(message)
print('\n'.join(messages))