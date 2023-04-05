sheeps_and_wolf = input().split(", ")
sheep_counter = 0
for anim in range(len(sheeps_and_wolf) - 1, -1, -1):
    sheep_counter += 1
    if sheeps_and_wolf[anim] == "wolf":
        sheep_counter -= 1
        if anim != len(sheeps_and_wolf) - 1:
            print(f"Oi! Sheep number {sheep_counter}! You are about to be eaten by a wolf!")
            break
        else:
            print("Please go away and stop eating my sheep")
            break
