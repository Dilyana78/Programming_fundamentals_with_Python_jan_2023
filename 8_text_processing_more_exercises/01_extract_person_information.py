lines = int(input())

for i in range(lines):
    person_information = input()
    index_1 = person_information.index("@")
    index_2 = person_information.index("|")
    name = person_information[index_1 + 1:index_2]
    index_3 = person_information.index("#")
    index_4 = person_information.index("*")
    age = person_information[index_3 + 1:index_4]
    print(f"{name} is {age} years old.")