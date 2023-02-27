int_health = 100
current_health = int_health
bitcoins = 0
rooms = input().split("|")
counter_rooms = 0
dead = False
for room in rooms:
    counter_rooms += 1
    room = room.split()
    command = room[0]
    number = int(room[1])
    if command == "potion":
        if current_health + number > int_health:
            diff = int_health - current_health
            current_health = int_health
            print(f"You healed for {diff} hp.")
        else:
            current_health += number
            print(f"You healed for {number} hp.")
        print(f"Current health: {current_health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        current_health -= number
        if current_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {counter_rooms}")
            dead = True
            break
if not dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {current_health}")