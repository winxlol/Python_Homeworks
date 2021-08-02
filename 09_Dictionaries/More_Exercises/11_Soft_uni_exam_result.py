from collections import defaultdict

students = {}
language_submissions = defaultdict(int)

while True:
    data = input()

    if data == "exam finished":
        break

    student_info = data.split("-")
    if len(student_info) > 2:
        username = student_info[0]
        language = student_info[1]
        points = int(student_info[2])

        if username not in students:
            students[username] = []

        if language not in students[username]:
            students[username].append(language)
            students[username].append(points)
        else:
            index = students[username].index(language)
            if points > students[username][index + 1]:
                students[username][index + 1] = points

        language_submissions[language] += 1

    else:
        username = student_info[0]

        students.pop(username)

students = sorted(students.items(), key=lambda x: (-x[1][1], x[1]))

print("Results:")
for student_name, student_result in students:
    print(f"{student_name} | {student_result[1]}")

language_submissions = sorted(language_submissions.items(), key=lambda x: (-x[1], x[0]))

print("Submissions:")
for language, count in language_submissions:
    print(f"{language} - {count}")