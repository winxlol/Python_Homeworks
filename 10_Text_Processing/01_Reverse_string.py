def reverse_string(word):
    return word[::-1]


word = input()
while word != "end":
    print(f"{word} = {reverse_string(word)}")
    word = input()