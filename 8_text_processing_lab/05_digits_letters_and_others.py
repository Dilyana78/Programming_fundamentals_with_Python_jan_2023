string = input()
digits = ""
letters = ""
chars = ""
for char in string:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        chars += char
print(f"{digits}\n{letters}\n{chars}")

# 2 version with lists
# text = input()
# digits = []
# letters = []
# other = []
# for char in text:
#     if char.isdigit():
#         digits.append(char)
#     elif char.isalpha():
#         letters.append(char)
#     else:
#         other.append(char)
# print(''.join(digits))
# print(''.join(letters))
# print(''.join(other))