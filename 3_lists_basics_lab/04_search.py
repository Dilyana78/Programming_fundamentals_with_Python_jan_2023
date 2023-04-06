number_of_lines = int(input())
word = input()
list_text = []
list_text_1 = []
for i in range(number_of_lines):
    current_text = input()
    list_text.append(current_text)
    if word in current_text:
        list_text_1.append(current_text)
print(list_text)
print(list_text_1)