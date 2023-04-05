n = int(input())

for i in range(1, n +1):
    current_num = int(input())
    if current_num % 2 != 0:
        print(f"{current_num} is odd!")
        exit()
print("All numbers are even.")

# 2_version

# number = int(input())

# for i in range(1, number + 1):
#     num = int(input())

#     if num % 2 != 0:
#         break
# if num % 2 != 0:
#     print(f"{num} is odd!")
# else:
#     print("All numbers are even.")