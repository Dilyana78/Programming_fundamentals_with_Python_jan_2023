int_energy = int(input())
user_input = input()
won_battles = 0
while user_input != "End of battle":
    distance = int(user_input)
    if int_energy >= distance:
        won_battles += 1
        int_energy -= distance
    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {int_energy} energy")
        exit()
    if won_battles % 3 == 0:
        int_energy += won_battles
    user_input = input()


print(f"Won battles: {won_battles}. Energy left: {int_energy}")
