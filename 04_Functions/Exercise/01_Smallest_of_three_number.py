def find_smallest_number(data):
    smallest_number = min(data)
    return smallest_number


num_one = int(input())
num_two = int(input())
num_three = int(input())

list_numbers = [num_one, num_two, num_three]

print(find_smallest_number(list_numbers))