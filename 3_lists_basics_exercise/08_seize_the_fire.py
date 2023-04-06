fire_info = input().split("#")
water = int(input())
effort = 0
put_out_water = []
for info in fire_info:
    current_info = info.split(" = ")
    fire_type = current_info[0]
    value = int(current_info[1])
    if water >= value:
        if (fire_type == "High" and 81 <= value <= 125) or (fire_type == "Medium" and 51 <= value <= 80) or \
                (fire_type == "Low" and 1 <= value <= 50):
            water -= value
            put_out_water.append(value)
            effort += value * 0.25
print(f"Cells:")
for cell in put_out_water:
    print(f" - {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_water)}")
