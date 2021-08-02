from collections import defaultdict

students = defaultdict(dict)


while True:
    data = input()

    if ":" not in data:
        current_course = data.split("_")
        current_course = " ".join(current_course)
        if current_course in students:
            for student, id in students[current_course].items():
                print(f"{student} - {id}")
        break

    tokens = data.split(":")
    name = tokens[0]
    student_id = int(tokens[1])
    course = tokens[2]

    students[course][name] = student_id

