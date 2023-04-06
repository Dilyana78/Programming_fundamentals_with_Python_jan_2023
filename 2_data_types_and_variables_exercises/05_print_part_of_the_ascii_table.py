first_char = int(input())
last_char = int(input())

for i in range(first_char, last_char + 1):
    print(chr(i), end=" ")

# 2_version
# start = int(input())
# final = int(input())
# for i in range(start, final + 1):
#     print(f"{chr(i)}", end=" ")