initial_string = input()
non_numbers = []
numbers = []
for i in initial_string:
    if i.isdigit():
        numbers.append(i)
    else:
        non_numbers.append(i)
take_list = [int(numbers[x]) for x in range(len(numbers)) if x % 2 == 0]
skip_list = [int(numbers[x]) for x in range(len(numbers)) if x % 2 != 0]

result = ''
number_of_iteration = len(take_list)
for _ in range(number_of_iteration):
    taken_letters = take_list.pop(0)
    result += ''.join([x for x in non_numbers[:taken_letters]])
    non_numbers = non_numbers[taken_letters:]
    skipped_letters = skip_list.pop(0)
    non_numbers = non_numbers[skipped_letters:]
print(result)
