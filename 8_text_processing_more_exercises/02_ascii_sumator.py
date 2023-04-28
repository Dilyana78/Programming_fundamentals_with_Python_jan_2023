start_char = input()
end_char = input()
random_chars = input()
result = 0
for char in random_chars:
    if ord(start_char) < ord(char) < ord(end_char):
        result += ord(char)
print(result)
