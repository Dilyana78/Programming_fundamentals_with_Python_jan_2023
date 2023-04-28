morse_code = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..'}

words = input().split(" | ")
final = ""

for word in words:
    morse_code_letters = word.split()
    for morse_code_letter in morse_code_letters:
        final += " ".join(key for key in morse_code if morse_code[key] == morse_code_letter)
    final += " "

print(final)


# 2 version
# morse_code = {".-": "A", "-...": "B",  "-.-.": "C", "-..": "D", ".": "E", "..-.":  "F", "--.": "G",
#               "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
#               "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S","-":  "T", "..-": "U",
#               "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"
#
# }
#
# message = ""
# text = input().split("|")
# for word in text:
#     every_word = word.split()
#     for elem in every_word:
#         if elem in morse_code:
#             message += morse_code[elem]
#     message += " "
# print(message)





#2 - a solution with list:
#
# morse_code = {'A': '.-', 'B': '-...',
#               'C': '-.-.', 'D': '-..', 'E': '.',
#               'F': '..-.', 'G': '--.', 'H': '....',
#               'I': '..', 'J': '.---', 'K': '-.-',
#               'L': '.-..', 'M': '--', 'N': '-.',
#               'O': '---', 'P': '.--.', 'Q': '--.-',
#               'R': '.-.', 'S': '...', 'T': '-',
#               'U': '..-', 'V': '...-', 'W': '.--',
#               'X': '-..-', 'Y': '-.--', 'Z': '--..'}
#
# words = input().split(" | ")
# final = []
#
# for word in words:
#     morse_code_letters = word.split()
#     for morse_code_letter in morse_code_letters:
#         [final.append(key) for key in morse_code if morse_code[key] == morse_code_letter]
#     final.append(" ")
#
# print(*final, sep="")