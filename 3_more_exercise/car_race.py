car_times = [int(x) for x in input().split()]

left_part = car_times[:len(car_times) // 2]
right_part = list(reversed(car_times[len(car_times) // 2 + 1:]))
left_sum = 0
right_sum = 0
for i in left_part:
    if i > 0:
        left_sum += i
    elif i == 0:
        left_sum = left_sum * 0.8
for i in right_part:
    if i > 0:
        right_sum += i
    elif i == 0:
        right_sum = right_sum * 0.8
winner = ""
if left_sum > right_sum:
    winner = "right"
else:
    winner = "left"

print(f"The winner is {winner} with total time: {min(left_sum, right_sum):.1f}")