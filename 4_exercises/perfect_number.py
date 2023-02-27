def perfect_number(some_number):
    sum_divisors = 0
    for i in range(1, some_number // 2):
        if some_number % i == 0:
            sum_divisors += i
    if sum_divisors * 2 == some_number:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfect_number(number))
