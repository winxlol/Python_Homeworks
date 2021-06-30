def check_vowels(data, vowels):
    word_no_vowels = [vowel for vowel in data if vowel not in vowels]
    return word_no_vowels


data = input()
vowels = "AaEeIiOoUu"

print("".join(check_vowels(data, vowels)))
