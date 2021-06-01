import sys
number = input()

separete_single_numbers_list = []
largest_single_number = -sys.maxsize
largest_number = ""

for num in number:
    num = int(num)
    separete_single_numbers_list.append(num)

while True:
    if len(separete_single_numbers_list) == 0:
        break

    for large in separete_single_numbers_list:
        if large >= largest_single_number:
            largest_single_number = large

    separete_single_numbers_list.remove(largest_single_number)
    largest_single_number = str(largest_single_number)
    largest_number += largest_single_number
    largest_single_number = -sys.maxsize

print(int(largest_number))