import sys

largest_number = -sys.maxsize

for _ in range(3):
    current_number = int(input())
    if current_number > largest_number:
        largest_number = current_number

print(largest_number)