def remove_str(data: str):
    return text.replace(data, len(data) * "*")


banned_words = input().split(", ")
text = input()

for word in banned_words:
    text = remove_str(word)

print(text)