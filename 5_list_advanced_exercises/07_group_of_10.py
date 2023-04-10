from math import ceil

numbers = [int(number) for number in input().split(", ")]
low_boundary = 1
high_boundary = 10
groups = ceil(max(numbers) / 10)

for idx in range(1, groups + 1):
    numbers_in_group = [x for x in numbers if low_boundary <= x <= high_boundary]
    print(f"Group of {idx * 10}'s: {numbers_in_group}")

    low_boundary += 10
    high_boundary += 10


# 2 version
# from math import ceil
# numbers = [int(x) for x in input().split(", ")]
# max_num = max(numbers)
# low_boundary = 1
# up_boundary = 10
#
# for num in numbers:
#     while up_boundary <= (ceil(max_num / 10)) * 10:
#         list_of_numbers = [num for num in numbers if low_boundary <= num <= up_boundary]
#         print(f"Group of {up_boundary}'s: {list_of_numbers}")
#         low_boundary += 10
#         up_boundary += 10

