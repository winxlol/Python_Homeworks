text = input().lower()

given_words_list = ['sand', 'water', 'fish', 'sun']

count = 0

for current_word in given_words_list:
    current_counts = text.count(current_word)
    count += current_counts

print(count)
