single_string = input()
upper_letters = [chr(x) for x in range(65, 91)]
list_of_capitals = []
for i in range(len(single_string)):
    if single_string[i] in upper_letters:
        list_of_capitals.append(i)
print(list_of_capitals)
