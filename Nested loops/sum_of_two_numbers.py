a = int(input())
b = int(input())
magic_num = int(input())
counter = 0
magic = False
for i in range(a, b + 1):
    for j in range(a, b + 1):
        counter += 1
        if i + j == magic_num:
            magic = True
            break
    if magic:
        break
if magic:
    print(f"Combination N:{counter} ({i} + {j} = {magic_num})")
else:
    print(f"{counter} combinations - neither equals {magic_num}")
