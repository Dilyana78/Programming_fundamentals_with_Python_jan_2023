start = input()
end = input()
skip = input()
counter = 0
for i in range(ord(start), ord(end) + 1):
    for j in range(ord(start), ord(end) + 1):
        for k in range(ord(start), ord(end) + 1):
            if chr(i) == skip or chr(j) == skip or chr(k) == skip:
                continue
            else:
                counter += 1
                print(f"{chr(i)}{chr(j)}{chr(k)}", end=" ")
print(f"{counter}", end=" ")
