data = input()

text = list(reversed(data))

filtered_text = "".join(text)
text = int(filtered_text)

if text == int(data):
    print(text)
