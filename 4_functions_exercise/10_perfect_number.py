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


# 2 version
# def perfect_number(some_number):
#     sum_divisors = 0
#     for i in range(1, some_number):
#         if some_number % i == 0:
#             sum_divisors += i
#     if sum_divisors == some_number:
#         return "We have a perfect number!"
#     return "It's not so perfect."
#
#
# number = int(input())
# print(perfect_number(number))


# 3 version
# def perfect_number(some_number):
#     sum_divisors = 0
#     for i in range(1, some_number):
#         if some_number % i == 0:
#             sum_divisors += i
#     if sum_divisors == some_number:
#         return True


# number = int(input())
# perfect_num = perfect_number(number)
# if perfect_num:
#     print("We have a perfect number!")
# else:
#     print("It's not so perfect.")


# 4 version
# def perfect_number(some_number):
#     counter_divisors = 0
#     divisors = []
#     for i in range(1, some_number):
#         if some_number % i == 0:
#             counter_divisors += 1
#             divisors.append(i)
#     if sum(divisors) == some_number:
#         return True
#
#
# number = int(input())
# perfect_num = perfect_number(number)
# if perfect_num:
#     print("We have a perfect number!")
# else:
#     print("It's not so perfect.")
