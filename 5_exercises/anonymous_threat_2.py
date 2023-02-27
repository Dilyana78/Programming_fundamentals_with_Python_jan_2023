def is_index_valid(idx, seq):
    return 0 <= idx < len(seq)


single_string = input().split()
line_input = input()

while line_input != "3:1":
    current_command = line_input.split()
    command = current_command[0]
    if command == "merge":
        start = int(current_command[1])
        end = int(current_command[2])
        if is_index_valid(start, single_string):
            start = start
        else:
            start = 0
        if is_index_valid(end, single_string):
            end = end
        else:
            end = len(single_string) - 1
        first_part = single_string[0:start]
        merged_part = single_string[start:end + 1]
        merged_part = [''.join(merged_part)]
        final_part = single_string[end + 1:]
        single_string = first_part + merged_part + final_part
    elif command == "divide":
        index = int(current_command[1])
        partitions = int(current_command[2])
        divided_part = list(single_string[index])
        first_list = single_string[0:index]
        second_list = single_string[index + 1:]
        single_string.pop(index)
        if (len(divided_part) / 2) % partitions == 0:
            step = len(divided_part) // partitions
            new_list = [divided_part[idx:idx + step] for idx in range(0, len(divided_part), step)]
        else:
            step = len(divided_part) // partitions
            new_list = [divided_part[idx:idx + step] for idx in range(0, len(divided_part) - (step + 1), step)]
            new_list = new_list + divided_part[-(step + 1):]
        new_list = [''.join(x) for x in new_list]
        single_string = first_list + new_list + second_list

    line_input = input()
print(' '.join(single_string))
