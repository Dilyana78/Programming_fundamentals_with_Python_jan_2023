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