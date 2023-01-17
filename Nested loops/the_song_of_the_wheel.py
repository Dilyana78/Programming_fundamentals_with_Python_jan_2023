m = int(input())    #[4...144]
counter = 0
fourth_combination = ""
valid = False
fourth = False
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and a * b + c * d == m and 4 < m < 144:
                    valid = True
                    counter += 1
                    print(f"{a}{b}{c}{d}", end=" ")
                    if counter == 4:
                        fourth = True
                        fourth_combination = f"{a}{b}{c}{d}"

if fourth:
    print()
    print(f"Password: {fourth_combination}")
else:
    print()
    print("No!")
if not valid:
    print("No!")
