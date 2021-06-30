def find_palindrome_words(words):
    for word in words:
        if word == word[::-1]:
            palindrome_words.append(word)


data = input().split()
given_palindrome = input()
palindrome_words = []

find_palindrome_words(data)

print(palindrome_words)
if given_palindrome in palindrome_words:
    print(f"Found palindrome {palindrome_words.count(given_palindrome)} times")
else:
    print("Found palindrome 0 times")

