offers = input().split(", ")

offers_as_digits = []
for money in offers:
    offers_as_digits.append(int(money))

beggars = int(input())
final_sum = []
starting_position = 0
while starting_position < beggars:
    current_beggar_sum = 0
    for i in range(starting_position, len(offers_as_digits), beggars):
        current_beggar_sum += offers_as_digits[i]
    final_sum.append(current_beggar_sum)
    starting_position += 1

print(final_sum)

# 2 version
# money = input().split(", ")
# beggars = int(input())
# outcome_for_each_beggar = []
# start_position = 0
# sum_money = 0
#
# while True:
#     if start_position >= beggars:
#         break
#     for turn in range(start_position, len(money) + 1, beggars):
#         if turn >= len(money):
#             break
#         turn = int(money[turn])
#         sum_money += turn
#     outcome_for_each_beggar.append(sum_money)
#     start_position += 1
#     sum_money = 0
#
# print(outcome_for_each_beggar)