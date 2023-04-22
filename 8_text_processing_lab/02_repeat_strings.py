text = input().split()
new_list = []

for string in text:
    new_list.append(string * len(string))
print(''.join(new_list))

# text = input().split()
# new_list = []
#
# for string in text:
#     for i in range(len(string)):
#         new_list.append(string)
# print(''.join(new_list))

# version in one row
# [print(s * len(s), end="") for s in input().split()]