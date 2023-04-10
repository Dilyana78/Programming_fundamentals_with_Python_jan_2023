words = input().split()
word = input()
palindrome_words = []
counter = 0
for el in words:
    if el == el[::-1]:
        palindrome_words.append(el)
        if el[::-1] == word:
            counter += 1
print(palindrome_words)
print(f"Found palindrome {counter} times")

