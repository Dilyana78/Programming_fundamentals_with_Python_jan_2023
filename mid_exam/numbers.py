numbers = [int(x) for x in input().split()]

avg_number = sum(numbers) / len(numbers)

greater_than_avg = []
for num in numbers:
    if num > avg_number:
        greater_than_avg.append(num)

sorted_greater = sorted(greater_than_avg, key=lambda x: - x)
greater_str = list(map(str, sorted_greater))

if len(greater_than_avg) == 0:
    print("No")
else:
    print(' '.join(greater_str[:5]))