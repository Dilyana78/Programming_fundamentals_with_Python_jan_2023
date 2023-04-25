some_string = input()
new_string = ""
strength = 0
for index in range(len(some_string)):
    if strength > 0 and some_string[index] != ">":
        strength -= 1
    elif some_string[index] == ">":
        new_string += some_string[index]
        strength += int(some_string[index + 1])
    else:
        new_string += some_string[index]
print(new_string)


# 2 version
# text = input()
# parts = text.split(">")
# previous = 0
#
# result = [parts[0]]
# for part in parts[1:]:
#     power = int(part[0])
#     previous += power
#
#     formatted_part = part[previous:]
#     previous = max(previous - len(part), 0)
#     result.append(formatted_part)
#
# print('>'.join(result))




