# numbers = [int(num) for num in input().split(", ")]
# positive_numbers = [num for num in numbers if num >= 0]
# negative_numbers = [num for num in numbers if num < 0]
# even_numbers = [num for num in numbers if num % 2 == 0]
# odd_numbers = [num for num in numbers if num % 2 != 0]
# print(f"Positive: {', '.join(str(num) for num in positive_numbers)}")
# print(f"Negative: {', '.join(str(num) for num in negative_numbers)}")
# print(f"Even: {', '.join(str(num) for num in even_numbers)}")
# print(f"Odd: {', '.join(str(num) for num in odd_numbers)}")

def positive_numbers(some_numbers):
    return [number for number in some_numbers if int(number) >= 0]


def negative_number(some_numbers):
    return [number for number in some_numbers if int(number) < 0]


def even_numbers(some_numbers):
    return [number for number in some_numbers if int(number) % 2 == 0]


def odd_numbers(some_numbers):
    return [number for number in some_numbers if int(number) % 2 != 0]


numbers = input().split(", ")
print(f"Positive: {', '.join(positive_numbers(numbers))}")
print(f"Negative: {', '.join(negative_number(numbers))}")
print(f"Even: {', '.join(even_numbers(numbers))}")
print(f"Odd: {', '.join(odd_numbers(numbers))}")
