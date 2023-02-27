number_of_rooms = int(input())
free_chairs = 0
not_enough_chairs = False
for room in range(1, number_of_rooms + 1):
    chairs, visitors = input().split(" ")
    if len(chairs) < int(visitors):
        diff = int(visitors) - len(chairs)
        print(f"{diff} more chairs needed in room {room}")
        not_enough_chairs = True
    else:
        free_chairs += len(chairs) - int(visitors)
if not not_enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")

