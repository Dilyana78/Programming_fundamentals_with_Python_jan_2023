distances = [int(x) for x in input().split()]

index = int(input())
total = 0
while True:
    if index < 0:
        removed = distances.pop(0)
        copied_el = distances[-1]
        distances.insert(0, copied_el)
        for i in range(len(distances)):
            if distances[i] <= removed:
                distances[i] += removed
            else:
                distances[i] -= removed
    elif index >= len(distances):
        removed = distances.pop(-1)
        copied_el = distances[0]
        distances.append(copied_el)
        for i in range(len(distances)):
            if distances[i] <= removed:
                distances[i] += removed
            else:
                distances[i] -= removed

    else:
        removed = distances.pop(index)
        for i in range(len(distances)):
            if distances[i] <= removed:
                distances[i] += removed
            else:
                distances[i] -= removed
    total += removed
    if len(distances) == 0:
        break
    index = int(input())
print(total)

# 2 version
# distance = [int(x) for x in input().split()]
# removed = []
# while len(distance) > 0:
#     index = int(input())
#     if index < 0:
#         removed_num = distance[0]
#         distance[0] = distance[-1]
#         distance = [x + removed_num if x <= removed_num else x - removed_num for x in distance]
#     elif index > len(distance) - 1:
#         removed_num = distance[-1]
#         distance[-1] = distance[0]
#         distance = [x + removed_num if x <= removed_num else x - removed_num for x in distance]
#     else:
#         removed_num = distance.pop(index)
#         distance = [x + removed_num if x <= removed_num else x - removed_num for x in distance]
#     removed.append(removed_num)
# print(sum(removed))