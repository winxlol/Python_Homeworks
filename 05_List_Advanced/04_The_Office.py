employees_happiness = list(map(int, input().split()))
factor = int(input())

employees_happiness = list(map(lambda x: x * factor, employees_happiness))

average_happiness = sum(employees_happiness) / len(employees_happiness)

happy_people = 0

for employee in employees_happiness:
    if employee > average_happiness:
        happy_people += 1

if happy_people >= len(employees_happiness) / 2:
    print(f"Score: {happy_people}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_people}/{len(employees_happiness)}. Employees are not happy!")
