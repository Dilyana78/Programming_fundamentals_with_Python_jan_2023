def odd_and_even_sum(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for num in number:
        digit = int(num)
        if digit % 2 == 0:
            sum_of_even_digits += digit
        else:
            sum_of_odd_digits += digit
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


number_as_string = input()
print(odd_and_even_sum(number_as_string))