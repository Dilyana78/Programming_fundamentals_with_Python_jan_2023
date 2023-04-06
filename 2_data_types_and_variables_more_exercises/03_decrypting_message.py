key = int(input())
lines = int(input())

for line in range(1, lines + 1):
    letter = input()
    new_letter = ord(letter) + key
    print(f"{chr(new_letter)}", end="")