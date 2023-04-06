water_tank_capacity = 255
number_of_lines = int(input())
pour_litres = 0
for flows in range(1, number_of_lines + 1):
    litres = int(input())
    if water_tank_capacity - litres < 0:
        print("Insufficient capacity!")
        continue
    pour_litres += litres
    water_tank_capacity -= litres

print(pour_litres)