def get_contests():
    contests = {}
    while True:
        command = input()
        if ':' not in command:
            break
        contest, password = command.split(':')
        contests[contest] = password
    return contests


def get_submissions(contests: dict):
    submissions = {}
    while True:
        command = input()
        if '=>' not in command:
            break
        contest, password, username, points = command.split('=>')
        points = int(points)
        if contest in contests and password == contests[contest]:  # validation check
            if username not in submissions:
                submissions[username] = {points: contest}
            else:
                for k, v in submissions[username].items():  # checking for the contest
                    if v == contest:
                        if k < points:  # comparing new and old points
                            k = points
                        break
                else:
                    submissions[username][points] = contest
    return submissions


def print_rankings(submssions: dict):
    sorted_names = sorted(submssions.keys())
    print(f"Ranking:")
    for name in sorted_names:
        print(name)
        sorted_points = sorted(submssions[name].keys(), reverse=True)  # sort in descending order
        for points in sorted_points:
            print(f"#  {submssions[name][points]} -> {points}")


contests = get_contests()
submissions = get_submissions(contests)
total_points = {sum(value): key for key, value in submissions.items()}  # total points for each person
print(f"Best candidate is {total_points[max(total_points)]} with total {max(total_points)} points.")
print_rankings(submissions)

# for key, value in data_per_user.items():
# #     results[key] = sum(value.values())
# #
# # best_score = max(results.values())
# # best_user = list(results.keys())[list(results.values()).index(best_score)]