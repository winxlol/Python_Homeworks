def log_in_details():
    while True:
        log_in_details = input()

        if log_in_details == "end of contests":
            break

        contest, password = log_in_details.split(":")

        if contest not in contests_log_in_details:
            contests_log_in_details[contest] = password


def username_input():
    while True:
        data = input()

        if data == "end of submissions":
            break

        username_details = data.split("=>")

        contest = username_details[0]
        password = username_details[1]
        username = username_details[2]
        points = int(username_details[3])

        if contest in contests_log_in_details and contests_log_in_details[contest] == password:
            if username not in students:
                students[username] = {}

                if contest not in students[username]:
                    students[username][contest] = points
            elif username in students and contest not in students[username].keys():
                students[username][contest] = points
            elif username in students and contest in students[username].keys():

                if points > students[username][contest]:
                    students[username][contest] = points


contests_log_in_details = {}
students = {}

log_in_details()
username_input()

total_points_per_student = {}

for name, details in students.items():
    total_points_per_student[name] = sum(details.values())

best_student = list(sorted(total_points_per_student.items(), key=lambda x: -x[1]))

print(f"Best candidate is {best_student[0][0]} with total {best_student[0][1]} points.")
print("Ranking:")

students_sorted_by_name = sorted(students.items())

for student_name, student_details in students_sorted_by_name:
    print(f"{student_name}")
    details_ordered_by_points = sorted(student_details.items(), key=lambda x: -x[1])
    for contest, points in details_ordered_by_points:
        print(f"#  {contest} -> {points}")



