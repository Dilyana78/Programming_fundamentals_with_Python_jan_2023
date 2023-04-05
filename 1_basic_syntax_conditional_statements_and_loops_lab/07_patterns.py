n = int(input())

for i in range(1, n + 1):
    print("*" * i)

for j in range(n - 1, 0, -1):
    print("*" * j)

# 2_version

# number = int(input())
# letter = "*"
# for i in range(1, number + 1):
#     for j in range(0, i):
#         print("*", end="")
#     print()
# for i in range(number - 1, 0, -1):
#     for j in range(0, i):
#         print("*", end="")
#     print()