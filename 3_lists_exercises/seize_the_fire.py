level_of_fire = input().split("#")
amount_of_water = int(input())
effort = 0
total_fire = 0
cells_water = []
for level in level_of_fire:
    level = level.split()
    type_of_fire = level[0]
    range_of_water = int(level[2])
    if ((type_of_fire == "High" and 81 <= range_of_water <= 125)
        or (type_of_fire == "Medium" and 51 <= range_of_water <= 80)
        or (type_of_fire == "Low" and 1 <= range_of_water <= 50)) and amount_of_water > range_of_water:
        effort += range_of_water * 0.25
        amount_of_water -= range_of_water
        cells_water.append(range_of_water)
        total_fire += range_of_water
    else:
        continue

print("Cells:")
for i in cells_water:
    print(f"- {i}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
