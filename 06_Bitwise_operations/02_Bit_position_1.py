def convert_to_binary(num):
    binary_digit = []

    while num > 0:
        if num % 2 == 0:
            num //= 2
            binary_digit.append(0)
        else:
            num //= 2
            binary_digit.append(1)

    binary_digit = list(reversed(binary_digit))

    return binary_digit


def find_position(binary_digit):
    return binary_digit[-2]


number = int(input())
bit_position = 1

print(convert_to_binary(number))
print(find_position(convert_to_binary(number)))

