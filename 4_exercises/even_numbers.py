list_of_integers = [int(num) for num in input().split()]

even = filter(lambda x: x % 2 == 0, list_of_integers)
print(list(even))
