def final_result(text, some_input):
    if text == "int":
        return int(some_input) * 2
    elif text == "real":
        return f"{float(some_input) * 1.5:.2f}"
    elif text == "string":
        return f"${some_input}$"


string_input = input()
data_type = input()
print(final_result(string_input, data_type))