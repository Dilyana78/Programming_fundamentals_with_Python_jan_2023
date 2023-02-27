days = int(input())
players = int(input())
energy = float(input())
water_per_day = float(input())
food_per_day = float(input())
total_water = days * players * water_per_day
total_food = days * players * food_per_day
no_energy = False
for day in range(1, days + 1):
    energy_lost = float(input())
    if energy > energy_lost:
        energy -= energy_lost
    else:
        no_energy = True
        break
    if day % 2 == 0:
        energy += energy * 0.05
        total_water -= total_water * 0.3
    if day % 3 == 0:
        total_food -= total_food / players
        energy += energy * 0.1

if no_energy:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
