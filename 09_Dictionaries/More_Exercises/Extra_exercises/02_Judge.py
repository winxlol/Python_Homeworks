from collections import defaultdict
contest_results = {}

while True:
    data = input()

    if data == "no more time":
        break

    details = data.split(" -> ")

    username = details[0]
    contest = details[1]
    points = int(details[2])

    if contest not in contest_results:
        contest_results[contest] = {}

    if username not in contest_results[contest]:
        contest_results[contest][username] = points
    else:
        if points > contest_results[contest][username]:
            contest_results[contest][username] = points

indivual_standings = defaultdict(int)
index = 0


for contest, names in contest_results.items():
    print(f"{contest}: {len(names)} participants")
    for name, points in sorted(names.items(), key=lambda kvp: (-kvp[1], kvp[0])):
        index += 1
        print(f"{index}. {name} <::> {points}")

        indivual_standings[name] += points
    index = 0

print("Individual standings:")
for key, value in sorted(indivual_standings.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    index += 1
    print(f"{index}. {key} -> {value}")
