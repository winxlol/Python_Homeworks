import math
people = int(input())
capacity = int(input())

if people % capacity == 0:
    total_courses = people / capacity
    print(round(total_courses))
else:
    courses = people / capacity
    print(math.ceil(courses))
