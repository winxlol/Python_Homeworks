def multiply_operator(num1, num2):
    return num1 * num2


def divide_operator(num1, num2):
    return int(num1 / num2)


def add_operator(num1, num2):
    return num1 + num2


def subtract_operator(num1, num2):
    return num1 - num2


operator = input()
num1 = int(input())
num2 = int(input())

if operator == "multiply":
    print(multiply_operator(num1, num2))
elif operator == "divide":
    print(divide_operator(num1, num2))
elif operator == "add":
    print(add_operator(num1,num2))
elif operator == "subtract":
    print(subtract_operator(num1, num2))


