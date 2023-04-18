data = input()
items = []
resources = {}
while data != "stop":
    items.append(data)
    data = input()
for i in range(0, len(items), 2):
    if items[i] not in resources:
        resources[items[i]] = 0
    resources[items[i]] += int(items[i + 1])
for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")

# 2 version with comprehension
# line = input()
# resources = {}
# while True:
#     if line == "stop":
#         break
#
#     quantity = int(input())
#     if line not in resources:
#         resources[line] = quantity
#     else:
#         resources[line] += quantity
#     line = input()
#
# result = {f"{resource} - {quantity}"for resource, quantity in resources.items()}

# print('\n'.join(result))
