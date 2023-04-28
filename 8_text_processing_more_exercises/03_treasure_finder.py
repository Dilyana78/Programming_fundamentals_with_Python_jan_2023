key = [int(x) for x in input().split()]
while True:
    line = input()
    if line == "find":
        break

    parts = len(line) // len(key)
    last_part_index = parts * len(key)
    last_part = line[last_part_index:]
    final_message = ''
    counter = 1
    for part in range(parts):
        next_index = len(key) * counter
        previous_index = next_index - len(key)
        current_part = line[previous_index:next_index]
        current_part = list(current_part)
        digit_current_part = [ord(char) for char in current_part]

        changed_list = [x - y for x, y in zip(digit_current_part, key)]
        nem_current_part = [chr(x) for x in changed_list]
        final_message += ''.join(nem_current_part)

        counter += 1

    for i in range(len(last_part)):
        new_char = chr(ord(last_part[i]) - key[i])
        final_message += new_char
    list_of_special = []
    for i in range(len(final_message)):
        if final_message[i] == "&":
            list_of_special.append(i)
        elif final_message[i] == "<":
            first_index = i
        elif final_message[i] == ">":
            last_index = i
    material = final_message[list_of_special[0] + 1:list_of_special[1]]
    location = final_message[first_index + 1:last_index]
    print(f"Found {material} at {location}")


# 2 version with functions

# key = list(map(int, input().split()))
#
#
# def find_items(curr_line, first_symbol, second_symbol):
#     start = curr_line.find(first_symbol)
#     end = curr_line.find(second_symbol, start + 1)
#     return curr_line[start + 1:end]
#
#
# while True:
#     command = input()
#     if command == "find":
#         break
#     line = list(command)
#     for i in range(len(line)):
#         num = key[i % len(key)]
#         line[i] = chr(ord(line[i]) - num)
#     final_line = "".join(line)
#
#     treasure_symbol = "&"
#     start_coordinates_symbol = "<"
#     end_coordinates_symbol = ">"
#     type_treasure = find_items(final_line, treasure_symbol, treasure_symbol)
#     coordinates = find_items(final_line, start_coordinates_symbol, end_coordinates_symbol)
#     print(f"Found {type_treasure} at {coordinates}")
