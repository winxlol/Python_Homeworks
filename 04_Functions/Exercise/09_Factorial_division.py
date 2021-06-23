def factorial_division(first_num, second_num):
    sum_first_num = first_num
    sum_second_num = second_num

    for current_num in range(first_num - 1, 0, -1):
        sum_first_num *= current_num

    for current_num in range(second_num - 1, 0, -1):
        sum_second_num *= current_num

    return sum_first_num / sum_second_num


first_num = int(input())
second_num = int(input())
numbers_divided_result = factorial_division(first_num, second_num)
print(f"{numbers_divided_result:.2f}")