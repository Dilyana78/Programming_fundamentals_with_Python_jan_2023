gifts = input().split()

text = input()

while text != "No Money":
    current_command = text.split()
    command = current_command[0]
    if command == "OutOfStock":
        gift = current_command[1]
        for i in range(len(gifts)):
            if gift in gifts[i]:
                gifts[i] = "None"
    elif command == "Required":
        gift = current_command[1]
        index = int(current_command[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift
    elif command == "JustInCase":
        gifts[-1] = current_command[1]

    text = input()

print(' '.join(i for i in gifts if i != "None"))