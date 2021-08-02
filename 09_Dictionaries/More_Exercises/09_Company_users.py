company_users = {}

while True:
    data = input().split(" -> ")

    if data[0] == "End":
        break

    company = data[0]
    user_id = data[1]

    if company not in company_users:
        company_users[company] = []

    if user_id not in company_users[company]:
        company_users[company].append(user_id)


sorted_by_company_name = sorted(company_users.items())

for key, value in sorted_by_company_name:
    print(f"{key}")

    for id in value:
        print(f"-- {id}")