budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price_lt = flour_price + (flour_price * 0.25)
price_per_loaf = flour_price + eggs_price + (milk_price_lt / 4)
eggs_counter = 0
bread_counter = 0
money = 0
int_budget = budget
while True:
    if budget < price_per_loaf or eggs_counter < 0:
        break
    bread_counter += 1
    budget -= price_per_loaf
    eggs_counter += 3
    money += price_per_loaf
    if bread_counter % 3 == 0:
        lost_eggs = bread_counter - 2
        eggs_counter -= lost_eggs

print(f"You made {bread_counter} loaves of Easter bread! Now you have {eggs_counter} eggs "
      f"and {int_budget - money:.2f}BGN left.")