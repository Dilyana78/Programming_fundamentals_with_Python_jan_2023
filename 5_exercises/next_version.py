version = [int(digit) for digit in input().split(".")]
version[-1] += 1

for digit in range(len(version) -1, -1, -1):
    if version[digit] > 9:
        version[digit] = 0
        if digit - 1 >= 0:
            version[digit - 1] += 1

print(".".join(str(digit) for digit in version))
