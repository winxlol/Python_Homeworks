numbers = list(map(int, input().split(", ")))

positive_list = [el for el in numbers if el >= 0]
negative_list = [el for el in numbers if el < 0]
even_list = [el for el in numbers if el % 2 == 0]
odd_list = [el for el in numbers if el % 2 == 1]

all_in_one = [positive_list, negative_list, even_list, odd_list]
name_lists = ['Positive', 'Negative', 'Even', 'Odd']

for index, current_name in enumerate(name_lists):
    all_in_one[index] = list(map(str, all_in_one[index]))
    print(f"{current_name}: ", end="")
    print(", ".join(all_in_one[index]))
