total_price = 0
total_without = 0
user_input = input()
while user_input != "special" and user_input != "regular":
    price_without_tax = float(user_input)
    if price_without_tax > 0:
        total_without += price_without_tax
    else:
        print("Invalid price!")

    user_input = input()

price_with_tax = total_without * 1.2
taxes = price_with_tax - total_without
if user_input == "special":
    price_with_tax = price_with_tax - (price_with_tax * 0.1)
if price_with_tax != 0:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_without:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {price_with_tax:.2f}$")
else:
    print("Invalid order!")