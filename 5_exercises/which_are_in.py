first_string = input().split(", ")
second_string = input().split(", ")
new_list = []
for word in first_string:
    for text in second_string:
        if word in text:
            new_list.append(word)
            break
print(new_list)