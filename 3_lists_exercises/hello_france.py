ticket = 150
list_of_items = input().split("|")
initial_budget = int(input())
budget = initial_budget
spent_money = 0
new_prices = []
for item in list_of_items:
    item = item.split("->")
    type_item = item[0]
    price_item = float(item[1])
    if ((type_item == "Clothes" and price_item <= 50) or (type_item == "Shoes" and price_item <= 35)
        or (type_item == "Accessories" and price_item <= 20.50)) and (budget >= price_item):
        budget -= price_item
        spent_money += price_item
        new_prices.append(price_item * 0.4 + price_item)
sold_items = spent_money * 0.4 + spent_money
profit = sold_items - spent_money
total_budget = budget + sold_items

for digit in new_prices:
    print(f"{digit:.2f}", end=" ")
print()
if total_budget >= ticket:
    print(f"Profit: {profit:.2f}")
    print("Hello, France!")
else:
    print(f"Profit: {profit:.2f}")
    print("Not enough money.")
