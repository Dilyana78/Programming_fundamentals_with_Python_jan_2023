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
