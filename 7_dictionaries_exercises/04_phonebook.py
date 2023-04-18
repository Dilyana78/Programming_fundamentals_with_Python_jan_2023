contact = input().split("-")
phonebook = {}
while True:
    if len(contact) == 1:
        count = int(contact[0])
        break
    name = contact[0]
    number = contact[1]
    phonebook[name] = number
    contact = input().split("-")

for i in range(count):
    some_name = input()
    if some_name in phonebook:
        print(f"{some_name} -> {phonebook[some_name]}")
    else:
        print(f"Contact {some_name} does not exist.")
