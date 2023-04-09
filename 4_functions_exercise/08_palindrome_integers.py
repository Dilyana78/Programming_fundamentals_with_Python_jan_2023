def palindrome_int(numbers):

    for num in positive_numbers:
        if num[::] == num[::-1]:
            print("True")
        else:
            print("False")


positive_numbers = input().split(", ")
palindrome_int(positive_numbers)