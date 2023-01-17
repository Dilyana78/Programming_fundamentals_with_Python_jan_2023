one_coins = int(input())
two_coins = int(input())
five_notes = int(input())
sum_money = int(input())
coins_sum_money = sum_money * 100

for one in range(0, (one_coins * 100) + 1, 100):
    for two in range(0, (two_coins * 200) + 1, 200):
        for five in range(0, (five_notes * 500) + 1, 500):
            if one + two + five == coins_sum_money:
                print(f"{one / 100:.0f} * 1 lv. + {two / 200:.0f} * 2 lv. + {five / 500:.0f} * 5 lv. = {sum_money} lv.")
