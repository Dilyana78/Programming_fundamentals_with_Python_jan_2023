while True:
    text = input()
    if text == "end":
        break
    print(f"{text} = {text[::-1]}")

# 2 version
# string = input()
# while True:
#     if string == "end":
#         break
#     reversed_string = ""
#     for i in range(len(string) - 1, - 1, -1):
#         reversed_string += string[i]
#     print(f"{string} = {reversed_string}")
#     string = input()