input_string = input().split()
characters = {}
for word in input_string:
    for letter in word:
        if letter not in characters:
            characters[letter] = 1
        else:
            characters[letter] += 1
for char, count in characters.items():
    print(f"{char} -> {count}")