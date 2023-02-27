def is_valid_index(inx, seq):
    return 0 <= inx < len(seq)


pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_health = int(input())
is_running = True
while is_running:
    command = input()

    if command == "Retire":
        break

    current_command = command.split()
    action = current_command[0]

    if action == "Fire":
        index = int(current_command[1])
        damage = int(current_command[2])
        if not is_valid_index(index, warship):
            continue
        warship[index] -= damage
        if warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            is_running = False

    elif action == "Defend":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        damage = int(current_command[3])
        if not is_valid_index(start_index, pirate_ship) or not is_valid_index(end_index, pirate_ship):
            continue
        for i in range(start_index, end_index + 1):
            pirate_ship[i] -= damage
            if pirate_ship[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                is_running = False
                break

    elif action == "Repair":
        index = int(current_command[1])
        health = int(current_command[2])
        if not is_valid_index(index, pirate_ship):
            continue
        pirate_ship[index] = min(max_health, pirate_ship[index] + health)

    elif action == "Status":
        status_health = max_health * 0.2
        counter = 0
        for i in pirate_ship:
            if i < status_health:
                counter += 1
        print(f"{counter} sections need repair.")

if is_running:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
