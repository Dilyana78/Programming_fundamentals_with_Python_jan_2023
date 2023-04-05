text = input()

while True:
    if text == "End":
        break
    if text == "SoftUni":
        text = input()
        continue
    for i in text:
        print(i * 2, end="")
    print()
    text = input()