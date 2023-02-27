numbers = input().split()
opposite_list = []
for number in numbers:
    current_number = -int(number)
    opposite_list.append(current_number)
print(opposite_list)