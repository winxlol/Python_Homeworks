from collections import defaultdict

data = input().lower().split()

words = defaultdict(int)

for current_word in data:
    words[current_word] += 1

searched_words = [key for key, value in words.items() if words[key] % 2 == 1]

print(" ".join(searched_words))