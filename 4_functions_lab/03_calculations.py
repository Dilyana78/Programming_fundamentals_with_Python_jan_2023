def calculation(operator, num_1, num_2):
    result = 0
    if operator == "multiply":
        result = num_1 * num_2
    elif operator == "divide":
        result = int(num_1 / num_2)
    elif operator == "add":
        result = num_1 * num_2
    elif operator == "subtract":
        result = num_1 - num_2
    return result


action = input()
number_1 = int(input())
number_2 = int(input())
print(calculation(action, number_1, number_2))
