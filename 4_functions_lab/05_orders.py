def total_price(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00
    return price * quantity


current_product = input()
quantity = int(input())
print(f"{total_price(current_product, quantity):.2f}")
