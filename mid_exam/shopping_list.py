products = input().split("!")
command = input()

while command != "Go Shopping!":
    current_command = command.split()
    action = current_command[0]
    product = current_command[1]
    if action == "Urgent":
        if product not in products:
            products.insert(0, product)
    elif action == "Unnecessary":
        if product in products:
            products.remove(product)
    elif action == "Correct":
        new_product = current_command[2]
        if product in products:
            idx = products.index(product)
            products[idx] = new_product
    elif action == "Rearrange":
        if product in products:
            products.remove(product)
            products.append(product)
    command = input()
print(', '.join(products))