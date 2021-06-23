def perfect_number(number: int):
    sum_of_num = 0
    divisor = 0
    while True:
        divisor += 1
        if number % divisor == 0:
            sum_of_num += divisor
            if number == sum_of_num:
                return "We have a perfect number!"

        if sum_of_num > number:
            return "It's not so perfect."


data = int(input())
print(perfect_number(data))