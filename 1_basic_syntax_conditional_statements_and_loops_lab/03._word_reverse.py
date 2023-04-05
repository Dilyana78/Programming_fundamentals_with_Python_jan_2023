word = input()
print(word[::-1])

# 2_version

# word = input()
# for i in range(len(word) -1, -1, -1):
#     print(f"{word[i]}", end="")

# 3_version

# word = input()
# reversed_word = ""
# for i in range(len(word) - 1, -1, -1):
#     print(f"{word[i]}", end="")

# 4_version with function

# def reverse(string):
# #     string = "".join(reversed(string))
# #     return string


# # word = input()

# # print("", end="")
# # print(reverse(word))
