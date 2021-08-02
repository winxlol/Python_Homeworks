from collections import defaultdict

data = input()
char_count_dict = defaultdict(int)

for char in data:
    if char != " ":
        char_count_dict[char] += 1

for key, value in char_count_dict.items():
    print(f"{key} -> {value}")