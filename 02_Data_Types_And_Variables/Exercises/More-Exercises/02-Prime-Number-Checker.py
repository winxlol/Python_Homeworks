number = int(input())

prime = 0

for divide in range(1, 10):
    if number % divide == 0:
        prime += 1

if prime < 3:
    print("True")
else:
    print("False")
