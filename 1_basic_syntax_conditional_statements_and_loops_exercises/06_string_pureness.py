n = int(input())
not_pure = False
for i in range(1, n + 1):
    text = input()
    for j in text:
        if j == "," or j == "." or j == "_":
            not_pure = True
            break
    if not_pure:
        print(f"{text} is not pure!")
    else:
        print(f"{text} is pure.")
    not_pure = False