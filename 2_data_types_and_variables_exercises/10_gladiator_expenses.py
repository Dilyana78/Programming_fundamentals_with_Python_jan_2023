lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmet_broken = lost_fights // 2
total_sward_broken = lost_fights // 3
total_shield_broken = lost_fights // 6
total_armor_broken = total_shield_broken // 2
expenses = total_helmet_broken * helmet_price + \
    total_sward_broken * sword_price + \
    total_shield_broken * shield_price + \
    total_armor_broken * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")

# 2_version
# lost_fights = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
# expenses = 0
# counter_shield = 0
# for i in range(1, lost_fights + 1):
#     if i % 2 == 0 and i % 3 == 0:
#         expenses += helmet_price + sword_price + shield_price
#         counter_shield += 1
#     elif i % 2 == 0:
#         expenses += helmet_price
#     elif i % 3 == 0:
#         expenses += sword_price
#     if counter_shield == 2:
#         expenses += armor_price
#         counter_shield = 0
# print(f"Gladiator expenses: {expenses:.2f} aureus")


