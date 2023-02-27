snowballs = int(input())
highest_value, h_weight, h_quality, h_time = 0, 0, 0, 0
for ball in range(1, snowballs + 1):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weight / time_needed) ** quality
    if value > highest_value:
        highest_value = value
        h_weight = weight
        h_quality = quality
        h_time = time_needed
print(f"{h_weight} : {h_time} = {int(highest_value)} ({h_quality})")