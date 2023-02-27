n = input()

for i in range(9, -1, -1):
    for j in n:
        if int(j) == int(i):
            print(j, end="")
