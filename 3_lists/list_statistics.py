number_of_lines = int(input())
positive_numbers = []
negative_numbers =[]

for i in range(number_of_lines):
    current_numbers = int(input())
    if current_numbers >= 0:
        positive_numbers.append(current_numbers)
    else:
        negative_numbers.append(current_numbers)
print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")