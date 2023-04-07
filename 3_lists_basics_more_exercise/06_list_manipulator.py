numbers = [int(x) for x in input().split()]
command = input()
min_odds = []
min_evens = []
max_odds = []
max_evens = []
evens = []
odds = []
while command != "end":
    current_command = command.split()
    if "exchange" in current_command:
        index = int(current_command[1])
        if not 0 <= index < len(numbers):
            print("Invalid index")
        else:
            numbers = numbers[index + 1:] + numbers[:index + 1]
    elif "max" in current_command:
        type_num = current_command[1]
        if type_num == "even":
            max_evens = [x for x in numbers if x % 2 == 0]
            if len(max_evens) == 0:
                print("No matches")
            else:
                max_even_num = max(max_evens)
                indexes = []
                for i, num in enumerate(numbers):
                    if num == max_even_num:
                        indexes.append(i)
                index_max_even = indexes[-1]
                print(index_max_even)
        elif type_num == "odd":
            max_odds = [x for x in numbers if x % 2 != 0]
            if len(max_odds) == 0:
                print("No matches")
            else:
                max_odd_num = max(max_odds)
                indexes = []
                for i, num in enumerate(numbers):
                    if num == max_odd_num:
                        indexes.append(i)
                index_max_odd = indexes[-1]
                print(index_max_odd)
    elif "min" in current_command:
        type_num = current_command[1]
        if type_num == "even":
            min_evens = [x for x in numbers if x % 2 == 0]
            if len(min_evens) == 0:
                print("No matches")
            else:
                min_even_num = min(min_evens)
                indexes = []
                for i, num in enumerate(numbers):
                    if num == min_even_num:
                        indexes.append(i)
                index_min_even = indexes[-1]
                print(index_min_even)
        elif type_num == "odd":
            min_odds = [x for x in numbers if x % 2 != 0]
            if len(min_odds) == 0:
                print("No matches")
            else:
                min_odd_num = min(min_odds)
                indexes = []
                for i, num in enumerate(numbers):
                    if num == min_odd_num:
                        indexes.append(i)
                index_min_odd = indexes[-1]
                print(index_min_odd)
    elif "first" in current_command:
        count, type_num = int(current_command[1]), current_command[2]
        if count > len(numbers):
            print("Invalid count")
        else:
            if type_num == "even":
                first_evens = []
                evens = [x for x in numbers if x % 2 == 0]
                if len(evens) == 0 or len(evens) < count:
                    print(evens)
                else:
                    for num in numbers:
                        if num % 2 == 0:
                            first_evens.append(num)
                            if len(first_evens) == count:
                                print(first_evens)
                                break
            elif type_num == "odd":
                first_odds = []
                odds = [x for x in numbers if x % 2 != 0]
                if len(odds) == 0 or len(odds) < count:
                    print(odds)
                else:
                    for num in numbers:
                        if num % 2 != 0:
                            first_odds.append(num)
                            if len(first_odds) == count:
                                print(first_odds)
                                break
    elif "last" in current_command:
        count, type_num = int(current_command[1]), current_command[2]
        if count > len(numbers):
            print("Invalid count")
        else:
            if type_num == "even":
                last_evens = []
                evens = [x for x in numbers if x % 2 == 0]
                if len(evens) == 0 or len(evens) < count:
                    print(evens)
                else:
                    for num in numbers:
                        if num % 2 == 0:
                            last_evens.append(num)
                        reversed_last_evens = reversed(last_evens[:count])
                        print(reversed(reversed_last_evens))
            elif type_num == "odd":
                last_odds = []
                odds = [x for x in numbers if x % 2 != 0]
                if len(odds) == 0 or len(odds) < count:
                    print(odds)
                else:
                    for num in numbers:
                        if num % 2 == 0:
                            last_odds.append(num)
                        reversed_last_odds = reversed(last_odds[:count])
                        print(reversed(reversed_last_odds))

    command = input()

print(numbers)