some_string = input()
new_string = ""
old_letter = ""
for char in some_string:
    if char == old_letter:
        continue
    else:
        new_string += char
    old_letter = char
print(new_string)