given_words = [word for word in input().lower().split(" ")]
word_count = {}
for word in given_words:
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1
for word, count in word_count.items():
    if count % 2 != 0:
        print(word, end=" ")


# words = input().split(" ")
# output = {}
#
# for word in words:
#     word_lower = word.lower()
#     if word_lower not in output:
#         output[word_lower] = 0
#     output[word_lower] += 1
# for key, value in output.items():
#     if output[key] % 2 != 0:
#         print(key, end=" ")