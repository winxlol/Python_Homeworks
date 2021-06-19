import sys
list_numbers = list(map(int, input().split()))
count = int(input())

smallest_number = sys.maxsize

for _ in range(count):
    for number in list_numbers:
        if number < smallest_number:
            smallest_number = number

    list_numbers.remove(smallest_number)
    smallest_number = sys.maxsize

final_result = map(str, list_numbers)
print(", ".join(final_result))
