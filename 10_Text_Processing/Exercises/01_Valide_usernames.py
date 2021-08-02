class ValidUsernames:
    def __init__(self):
        self.valid_usernames = []

    def valid_lenght(self, username):
        if 3 <= len(username) <= 16:
            return True
        return False

    def valid_containing_chars(self, username):
        for char in username:
            if char.isalnum() or char == "_" or char == "-":
                continue
            return False

    def valid_symbols(self, username):
        if self.valid_containing_chars(username) is None:
            return True
        else:
            return False

    def is_all_true(self, lenght, chars, symbols, word):
        if lenght and chars is None and symbols:
            self.valid_usernames.append(word)


usernames = input().split(", ")
valid_names = ValidUsernames()

for index in range(len(usernames)):
    lenght = valid_names.valid_lenght(usernames[index])
    correct_chars = valid_names.valid_containing_chars(usernames[index])
    symbols = valid_names.valid_symbols(usernames[index])

    valid_names.is_all_true(lenght, correct_chars, symbols, usernames[index])


print("\n".join(valid_names.valid_usernames))