word = input()

#print(word[::-1])
reversed_word = ""

for letter in reversed(word):
    reversed_word += letter

print(reversed_word)
