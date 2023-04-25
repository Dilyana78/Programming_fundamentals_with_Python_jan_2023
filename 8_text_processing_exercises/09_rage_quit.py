text = input()
new_text = ""
current_text = ""

for index in range(len(text)):
    symbol = text[index]
    if not symbol.isdigit():
        current_text += symbol.upper()
    elif symbol.isdigit():
        if index == len(text) - 1 and text[index - 1].isdigit():
            break
        elif index != len(text) - 1:
            current_number = ""
            for i in range(index, len(text)):
                if text[i].isdigit():
                    current_number += text[i]
                else:
                    break
            current_number = int(current_number)
            new_text += (current_text * current_number)
            current_text = ""
        else:
            new_text += (current_text * int(symbol))
            current_text = ""

print(f"Unique symbols used: {len(set(new_text))}")
print(new_text)