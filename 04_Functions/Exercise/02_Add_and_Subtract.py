def sum_numbers(num1, num2):
    return num1 + num2


def sub_numbers(sum_of_first_two_numbers, num3):
    return sum_of_first_two_numbers - num3


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(sub_numbers(sum_numbers(first_number, second_number), third_number))
