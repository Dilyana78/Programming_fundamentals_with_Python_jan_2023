budget = int(input())
price = input()
total_money = 0

while price != "End":
    price = int(price)
    total_money += price
    if budget < total_money:
        print("You went in overdraft!")
        break
    price = input()

else:
    print("You bought everything needed.")

# 2_version with flag

# budget = int(input())
# price = input()
# total_money = 0
# over = False
# while price != "End":
#     price = int(price)
#     total_money += price
#     if budget < total_money:
#         over = True
#         break
#     price = input()
# if over:
#     print("You went in overdraft!")
# else:
#     print("You bought everything needed.")

# 3_version

# budget = int(input())
# price = input()
# sum_products = 0
#
# while price != "End":
#      price = int(price)
#      sum_products += price
#      if sum_products > budget:
#          print("You went in overdraft!")
#          break
#      price = input()
# if budget >= sum_products:
#     print("You bought everything needed.")