from math import factorial
def factorial_of_two(num1, num2):
    division = 0
    list_factorial = []

    for num in list_of_two:
        final_product = factorial(num)
        list_factorial.append(final_product)
    division = list_factorial[0] / list_factorial[1]
    return f"{division:.2f}"


first_number = int(input())
second_number = int(input())
list_of_two = [first_number, second_number]
print(factorial_of_two(first_number, second_number))


# 2 version
# def factorial(number):
#     for num in range(1, number):
#         number *= num
#     return number
#
#
# first_number = int(input())
# second_number = int(input())
# first_factorial = factorial(first_number)
# second_factorial = factorial(second_number)
# result = first_factorial / second_factorial
# print(f"{result:.2f}")