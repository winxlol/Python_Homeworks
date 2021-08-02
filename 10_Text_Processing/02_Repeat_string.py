def repeat_string(data: str):
    return data * len(data)


tokens = input().split()

for token in range(len(tokens)):
    print(repeat_string(tokens[token]), end="")

