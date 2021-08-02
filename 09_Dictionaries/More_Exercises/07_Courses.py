courses = {}

while True:
    data = input().split(" : ")

    if data[0] == "end":
        break

    course = data[0]
    name = data[1]

    if course not in courses:
        courses[course] = []

    courses[course].append(name)

course_sortation = sorted(courses.items(), key=lambda x: -len(x[1]))

for key, value in course_sortation:
    print(f"{key}: {len(value)}")

    value = sorted(value)

    for current_name in value:
        print(f"-- {current_name}")