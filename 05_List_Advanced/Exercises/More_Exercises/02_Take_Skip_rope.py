data = input()
data = [el for el in data]

digit_list = [int(el) for el in data if el.isdigit()]
string_list = [el for el in data if not el.isdigit()]

take_list = [digit_list[el] for el in range(len(digit_list)) if el % 2 == 0]
skip_list = [digit_list[el] for el in range(len(digit_list)) if el % 2 == 1]

result = []
total_index = 0


for index in range(len(take_list)):

    if take_list[index] > 0:
        for take_index in range(total_index, total_index + take_list[index]):
            if take_index == len(string_list):
                break
            result.append(string_list[take_index])
        total_index += take_list[index]

    if skip_list[index] > 0:
        total_index += skip_list[index]

print("".join(result))

