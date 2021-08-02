rows = int(input())

book_grade = {}

for row in range(rows):
    student = input()
    grade = float(input())

    if student not in book_grade:
        book_grade[student] = []

    book_grade[student].append(grade)


for key, value in book_grade.items():
    book_grade[key] = sum(value) / len(value)

filtred_book_grade = [(name, value) for name, value in book_grade.items() if value >= 4.50]

filtred_book_grade = sorted(filtred_book_grade, key=lambda x: -x[1])

for student_name, student_grade in filtred_book_grade:
    print(f"{student_name} -> {student_grade:.2f}")