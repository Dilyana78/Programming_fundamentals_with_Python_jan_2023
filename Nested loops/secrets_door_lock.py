upper_first = int(input())
upper_second = int(input())
upper_third = int(input())

for i in range(2, upper_first + 1, 2):
    for j in range(2, upper_second + 1):
        for k in range(2, upper_third + 1, 2):
            if j == 2 or j == 3 or j == 5 or j == 7:
                print(f"{i} {j} {k}")
