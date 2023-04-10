first_string = input().split(", ")
second_string = input().split(", ")
new_list = []
for word in first_string:
    for text in second_string:
        if word in text:
            new_list.append(word)
            break
print(new_list)

# # 2 version
# first_string = input().split(", ")
# second_string = input().split(", ")
# new_list = []
# for word in first_string:
#     for text in second_string:
#         if word in text and word not in new_list:
#             new_list.append(word)
# print(new_list)