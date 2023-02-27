numbers = [int(x)for x in input().split(', ')]
for num in numbers:
    if num == 0:
        numbers.remove(0)
        numbers.append(0)
print(numbers)