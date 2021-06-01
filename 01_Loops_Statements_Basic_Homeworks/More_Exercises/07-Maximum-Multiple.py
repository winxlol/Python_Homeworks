import sys
divisor = int(input())
bound = int(input())

max_number = -sys.maxsize

for number in range(bound,1, -1):
    if number % divisor == 0:
        if number > max_number:
            max_number = number

print(max_number)
