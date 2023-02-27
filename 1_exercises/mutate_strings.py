string_one = input()
string_two = input()
new_string = string_one
for char in range(len(string_one)):
    if string_one[char] == string_two[char]:
        continue
    new_string = string_two[:char + 1] + string_one[char + 1:]
    print(new_string)
