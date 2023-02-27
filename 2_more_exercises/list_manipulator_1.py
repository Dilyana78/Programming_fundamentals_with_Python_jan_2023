def is_valid_index(inx, seq):
    return 0 <= inx < len(seq)


numbers = [int(x) for x in input().split()]
input_text = input()
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
while input_text != "end":
    current_command = input_text.split()
    command = current_command[0]
    if command == "exchange":
        index = int(current_command[1])
        if is_valid_index(index, numbers):
            first_part = numbers[:index + 1]
            second_part = numbers[index + 1:]
            numbers = second_part + first_part
        else:
            print("Invalid index")
    elif command == "max":
        even_odd = current_command[1]
        if even_odd == "even":
            if len(even_numbers) == 0:
                print("No matches")
            else:
                max_even = max(even_numbers)
                print(numbers.index(max_even))
        elif even_odd == "odd":
            if len(odd_numbers) == 0:
                print("No matches")
            else:
                max_odd = max(odd_numbers)
                print(numbers.index(max_odd))
    elif command == "min":
        even_odd = current_command[1]
        if even_odd == "even":
            if len(even_numbers) == 0:
                print("No matches")
            else:
                min_even = min(even_numbers)
                print(numbers.index(min_even))
        elif even_odd == "odd":
            if len(odd_numbers) == 0:
                print("No matches")
            else:
                min_odd = min(odd_numbers)
                print(numbers.index(min_odd))
    elif command == "first":
        first_even = []
        first_odd = []
        count = int(current_command[1])
        if count > len(numbers):
            print("Invalid count")
        else:
            counter = 0
            even_odd = current_command[2]
            if even_odd == "even":
                for num in numbers:
                    if num % 2 == 0:
                        first_even.append(num)
                        counter += 1
                        if counter == count:
                            break
                print(first_even)
            elif even_odd == "odd":
                for num in numbers:
                    if num % 2 != 0:
                        first_odd.append(num)
                        counter += 1
                        if counter == count:
                            break
                print(first_odd)
    elif command == "last":
        count = int(current_command[1])
        counter = 0
        if count > len(numbers):
            print("Invalid count")
        else:
            even_odd = current_command[2]
            if even_odd == "even":
                last_even = []
                for num in range(len(numbers) -1, -1, -1):
                    if numbers[num] % 2 == 0:
                        last_even.append(numbers[num])
                        counter += 1
                        if counter == count:
                            break
                print(last_even)
            elif even_odd == "odd":
                last_odd = []
                for num in range(len(numbers) -1, -1, -1):
                    if numbers[num] % 2 != 0:
                        last_odd.append(numbers[num])
                        counter += 1
                        if counter == count:
                            break
                print(last_odd)
    input_text = input()
print(numbers)