foods = input().split()
bakery = {}
for item in range(0, len(foods), 2):
    key = foods[item]
    value = int(foods[item + 1])
    bakery[key] = value
print(bakery)