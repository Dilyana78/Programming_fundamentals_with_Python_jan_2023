def is_index_is_valid(idx, seq):
    return 0 <= idx < len(seq)


input_string = input().split()
command = input()

while command != "3:1":
    current_command = command.split()
    action = current_command[0]
    if action == "merge":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if is_index_is_valid(start_index, input_string):
            start_index = start_index
        else:
            start_index = 0
        if is_index_is_valid(end_index, input_string):
            end_index = end_index
        else:
            end_index = len(input_string) - 1
        first_part = input_string[0:start_index]
        second_part = [''.join(input_string[start_index:end_index + 1])]
        third_part = input_string[end_index + 1:]
        input_string = first_part + second_part + third_part
    elif action == 'divide':
        index = int(current_command[1])
        partitions = int(current_command[2])
        if partitions > len(input_string[index]):
            step = 1
        else:
            step = len(input_string[index]) // partitions
        divide_part = input_string.pop(index)
        start = 0
        for parts in range(partitions):
            if parts == partitions - 1:
                input_string.insert(index, divide_part[start::])
                break
            else:
                input_string.insert(index, divide_part[start: start + step:])
            start += step
            index += 1
    command = input()
print(' '.join(input_string))