def is_valid_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def valid_character(name):
    for char in name:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True


def no_redundant_symbols(name):
    if " " in name:
        return False
    return True


def username_validation(name):
    if is_valid_length(name) and valid_character(name) and no_redundant_symbols(name):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_validation(username):
        print(username)