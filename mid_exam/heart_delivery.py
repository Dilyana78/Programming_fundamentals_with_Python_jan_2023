neighborhood = [int(n) for n in input().split("@")]
command = input()
jump_length = 0
while command != "Love!":
    current_command = command.split()
    jump_length += int(current_command[1])
    if jump_length > len(neighborhood) - 1:
        jump_length = 0
        if neighborhood[jump_length] == 0:
            print(f"Place {jump_length} already had Valentine's day.")
        else:
            neighborhood[jump_length] -= 2
            if neighborhood[jump_length] == 0:
                print(f"Place {jump_length} has Valentine's day.")
    else:
        if neighborhood[jump_length] == 0:
            print(f"Place {jump_length} already had Valentine's day.")
        else:
            neighborhood[jump_length] -= 2
            if neighborhood[jump_length] == 0:
                print(f"Place {jump_length} has Valentine's day.")
    command = input()
print(f"Cupid's last position was {jump_length}.")
counter = 0
for i in neighborhood:
    if i == 0:
        counter += 1
if counter == len(neighborhood):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood) - counter} places.")
