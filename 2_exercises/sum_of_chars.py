n_lines = int(input())
sum_of_letters = 0
for i in range(1, n_lines + 1):
    letter = input()
    sum_of_letters += ord(letter)
print(f"The sum equals: {sum_of_letters}")
