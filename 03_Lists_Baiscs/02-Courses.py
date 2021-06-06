attempts = int(input())

database = []

for attempt in range(attempts):
    current_name = input()
    database.append(current_name)

print(database)