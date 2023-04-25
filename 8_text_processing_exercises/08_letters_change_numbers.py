some_string = input().split()
results = []
for el in some_string:
    result = 0
    digits = []
    for char in el:
        if char.isdigit():
            digits.append(char)
    number = int(''.join(digits))
    front_letter = el[0]
    end_letter = el[-1]
    if front_letter.isupper():
        divisor = ord(front_letter) - 64
        result = number / divisor
    elif front_letter.islower():
        multiplier = ord(front_letter) - 96
        result = number * multiplier
    if end_letter.isupper():
        digit_to_subtract = ord(end_letter) - 64
        result -= digit_to_subtract
    elif end_letter.islower():
        digit_to_add = ord(end_letter) - 96
        result += digit_to_add
    results.append(result)
print(f"{sum(results):.2f}")




