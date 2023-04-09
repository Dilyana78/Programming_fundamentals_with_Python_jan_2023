def round_number(seq):
    rounded_numbers= []
    for num in seq:
        num = round(num)
        rounded_numbers.append(num)
    return rounded_numbers


numbers = [float(x) for x in input().split()]
print(round_number(numbers))