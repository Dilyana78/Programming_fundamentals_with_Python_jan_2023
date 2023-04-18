contests = {}
individual_standings = {}

while True:
    line = input()
    if line == "no more time":
        break
    command = line.split(" -> ")
    username, contest, points = command[0], command[1], int(command[2])
    contests[contest] = contests.get(contest, {})
    contests[contest][username] = contests[contest].get(username, 0)
    if points > contests[contest][username]:
        contests[contest][username] = points

    individual_standings[username] = individual_standings.get(username, {})
    individual_standings[username][contest] = individual_standings[username].get(contest, 0)
    if points > individual_standings[username][contest]:
        individual_standings[username][contest] = points

for name in contests.keys():
    second_dict_values = contests[name]
    print(f"{name}: {len(second_dict_values)} participants")

    for pos, (key, value) in enumerate(sorted(second_dict_values.items(), key=lambda x: (-x[1], x[0])), 1):
        print(f"{pos}. {key} <::> {value}")

new_dictionary = {}

for individual_name in individual_standings.keys():
    second_dict = individual_standings[individual_name]
    sum_points = sum(second_dict.values())
    new_dictionary[individual_name] = sum_points

print("Individual standings:")

for position, (key, value) in enumerate(sorted(new_dictionary.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{position}. {key} -> {value}")