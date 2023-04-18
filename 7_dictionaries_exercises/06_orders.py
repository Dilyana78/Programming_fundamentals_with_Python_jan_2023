price_by_product = {}
quantity_by_product = {}

while True:
    line = input()
    if line == "buy":
        break

    products = line.split()
    name = products[0]
    price = float(products[1])
    quantity = int(products[2])
    if name not in quantity_by_product:
        quantity_by_product[name] = quantity
    else:
        quantity_by_product[name] += quantity

    price_by_product[name] = price

for product in price_by_product:
    price = price_by_product[product]
    quantity = quantity_by_product[product]
    total_price = price * quantity
    print(f"{product} -> {total_price:.2f}")