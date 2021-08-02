def is_digit(char: str):
    if char.isdigit():
        return char
    else:
        return ""


def is_str(char: str):
    if char.isalpha():
        return char
    else:
        return ""


def is_symbol(char):
    if is_digit(char) == "" and is_str(char) == "":
        return char
    return ""


data = input()

digits = ""
strings = ""
symbols = ""

for char in data:
    digits += is_digit(char)
    strings += is_str(char)
    symbols += is_symbol(char)


print(digits)
print(strings)
print(symbols)