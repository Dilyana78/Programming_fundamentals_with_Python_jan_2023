given_text = input()
given_text= given_text.lower()
special_words = ["sand", "water", "fish", "sun"]
counter = 0
for item in special_words:
    if item in given_text:
        word_count = given_text.count(item)
        counter += word_count
print(counter)