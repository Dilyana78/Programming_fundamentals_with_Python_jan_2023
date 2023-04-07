seq_of_numbers = input().split()
message = input()
message = list(message)
secret_message = ""
for num in seq_of_numbers:
    index = 0
    for i in num:
        index += int(i)
    if index > len(message) - 1:
        index = index % len(message)
    letter = message.pop(index)
    secret_message += letter
print(secret_message)