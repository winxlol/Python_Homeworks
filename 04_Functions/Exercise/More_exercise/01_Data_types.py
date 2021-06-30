def int_num(num):
    return int(num) * 2


def real_num(num):
    return float(num) * 1.5


def string(text):
    return f"${text}$"


type = input()
data = input()

if type == "int":
    print(int_num(data))
elif type == "real":
    result = real_num(data)
    print(f"{result:.2f}")
elif type == "string":
    print(string(data))