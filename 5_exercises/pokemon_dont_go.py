distance = [int(x) for x in input().split()]
removed = []
while len(distance) > 0:
    index = int(input())
    if index < 0:
        removed_num = distance[0]
        distance[0] = distance[-1]
        distance = [x + removed_num if x <= removed_num else x - removed_num for x in distance]
    elif index > len(distance) - 1:
        removed_num = distance[-1]
        distance[-1] = distance[0]
        distance = [x + removed_num if x <= removed_num else x - removed_num for x in distance]
    else:
        removed_num = distance.pop(index)
        distance = [x + removed_num if x <= removed_num else x - removed_num for x in distance]
    removed.append(removed_num)
print(sum(removed))