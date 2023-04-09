def characters_in_range(first, last):
    list_of_chars = []
    for char in range(ord(first) + 1, ord(last)):
        current_char = chr(char)
        list_of_chars.append(current_char)
    return f" ".join(list_of_chars)


char1 = input()
char2 = input()
print(characters_in_range(char1, char2))