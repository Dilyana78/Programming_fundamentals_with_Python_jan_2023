number_of_lines = int(input())

command_even = "even"
command_odd = "odd"
command_positive = "positive"
command_negative = "negative"

numbers = []

for i in range(number_of_lines):
    current_number = int(input())
    numbers.append(current_number)

command = input()
filtered_numbers = []

for number in numbers:
    filtered_passed = (
        (command == command_even and number % 2 == 0) or
        (command == command_odd and number % 2 != 0) or
        (command == command_positive and number >= 0) or
        (command == command_negative and number < 0)
    )
    if filtered_passed:
        filtered_numbers.append(number)
print(filtered_numbers)

# 2 version
# number_of_lines = int(input())
# list_of_numbers = []
#
# for line in range(number_of_lines):
#     current_number = int(input())
#     list_of_numbers.append(current_number)
#
# command = input()
# filtered_list = []
# for num in list_of_numbers:
#     if command == "positive" and num >= 0:
#         filtered_list.append(num)
#     elif command == "negative" and num < 0:
#         filtered_list.append(num)
#     if command == "even" and num % 2 == 0:
#         filtered_list.append(num)
#     if command == "odd" and num % 2 != 0:
#         filtered_list.append(num)
# print(filtered_list)