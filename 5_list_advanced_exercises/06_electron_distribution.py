# number_of_electrons = int(input())
# filled_shells = []
# shell = 1
# while number_of_electrons > 0:
#     current_electrons = 2 * shell**2
#     if number_of_electrons > current_electrons:
#         number_of_electrons -= current_electrons
#     else:
#         current_electrons = number_of_electrons
#         number_of_electrons = 0
#     filled_shells.append(current_electrons)
#     shell += 1
# print(filled_shells)

number_of_electrons = int(input())
filled_shells = []

while number_of_electrons > 0:
    n = len(filled_shells) + 1
    value = min(2 * n**2, number_of_electrons)
    filled_shells.append(value)
    number_of_electrons -= value

print(filled_shells)