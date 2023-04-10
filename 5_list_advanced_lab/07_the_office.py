employees = [int(num) for num in input().split()]
happiness_improvement_factor = int(input())

happiness = list(map(lambda x: x * happiness_improvement_factor, employees))
filtered = list(filter(lambda x: x >= sum(happiness) / len(employees), happiness))

if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")