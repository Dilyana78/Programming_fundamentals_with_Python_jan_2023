def result(seq):
    for num in seq:
        if num == 0:
            return "zero"
        else:
            count_negative = 0
            if num < 0:
                count_negative += 1
    if count_negative == 1 or count_negative == 3:
        return "negative"
    elif count_negative == 0 or count_negative == 2:
        return "positive"


first_num = int(input())
second_num = int(input())
third_num = int(input())
list_of_numbers = [first_num, second_num, third_num]
print(result(list_of_numbers))