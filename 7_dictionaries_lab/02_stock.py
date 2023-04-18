products = input().split()
dictionary = {}
for item in range(0, len(products), 2):
    key = products[item]
    value = int(products[item + 1])
    dictionary[key] = value

searched_items = input().split()
for item in searched_items:
    if item in dictionary.keys():
        quantity = dictionary[item]
        print(f"We have {quantity} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")