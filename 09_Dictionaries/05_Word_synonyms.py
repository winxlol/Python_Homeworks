from collections import defaultdict

count = int(input())

dictionary_words = defaultdict(list)

for _ in range(count):
    word = input()
    synonym = input()

    dictionary_words[word].append(synonym)

for key, value in dictionary_words.items():
    print(f"{key} - {', '.join(value)}")
