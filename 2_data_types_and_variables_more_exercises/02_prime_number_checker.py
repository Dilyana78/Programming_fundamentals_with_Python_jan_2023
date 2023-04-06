n = int(input())
is_prime = True

for current_number in range(2, n):
    if n % current_number == 0:
        is_prime = False
        break
print(is_prime)

# 2_version
# n = int(input())
# counter = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         counter += 1
# if counter == 2:
#     print("True")
# else:
#     print("False")

# 3_version with flag
# n = int(input())
# counter = 0
# is_prime = False
# for i in range(1, n + 1):
#     if n % i == 0:
#         counter += 1
# if counter == 2:
#     is_prime = True
# print(is_prime)