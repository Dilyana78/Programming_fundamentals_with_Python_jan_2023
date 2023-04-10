def int_to_chr(word):
    string = list(word)
    num_as_str = list()

    while string[0].isdigit():
        num_as_str.append(string[0])
        string.pop(0)

    num = int(''.join(num_as_str))
    string.insert(0, chr(num))
    return ''.join(string)


def switch_letters(word):
    letters = list(word)
    letters[1], letters[-1] = letters[-1], letters[1]
    return ''.join(letters)


print(' '.join([switch_letters(int_to_chr(word)) for word in input().split()]))

# 2 version
# def replace_char_code(word: str):
#     ch_code_str = ''
#     new_word = []
#
#     for ch in word:
#         if ch.isnumeric():
#             ch_code_str += ch
#
#         else:
#             new_word.append(ch)

#     ch_at_beginning = chr(int(ch_code_str))
#
#     new_word.insert(0, ch_at_beginning)
#
#     return new_word
#
#
# def decipher_word(word: str):
#     new_word = replace_char_code(word)
#
#     new_word[1], new_word[-1] = new_word[-1], new_word[1]
#
#     return ''.join(new_word)

# 3 version
# words = input().split()
# result = []
# for word in words:
#     current_word = list(word)
#     num_list = []
#     while current_word[0].isdigit():
#         num_list.append(current_word[0])
#         current_word.pop(0)
#     num_list = "".join(num_list)
#     number = int(num_list)
#     letter = chr(number)
#     current_word.insert(0, letter)
#     current_word[1], current_word[-1] = current_word[-1], current_word[1]
#     current_word = "".join(current_word)
#     result.append(current_word)
#
# print(" ".join(result))