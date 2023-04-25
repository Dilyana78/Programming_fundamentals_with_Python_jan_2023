start_text = input()
encrypted_text = ""
for char in start_text:
    new_char = chr(ord(char) + 3)
    encrypted_text += new_char
print(encrypted_text)