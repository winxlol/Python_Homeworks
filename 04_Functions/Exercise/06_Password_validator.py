def password_validator(len, letters_and_digits, not_enough_digits):
    flag = True

    if not len:
        flag = False
        print("Password must be between 6 and 10 characters")

    if not letters_and_digits:
        flag = False
        print("Password must consist only of letters and digits")

    if not not_enough_digits:
        flag = False
        print("Password must have at least 2 digits")

    if flag:
        print("Password is valid")


def len_password(password):
    if 6 <= len(password) <= 10:
        return True
    else:
        return False


def letters_and_digits(password):
    if password.isalnum():
        return True
    else:
        return False


def not_enough_digits(password):
    counter = 0
    for char in password:
        if char.isdigit():
            counter += 1
        if counter > 1:
            return True

    return False


data = input()
password_validator(len_password(data), letters_and_digits(data), not_enough_digits(data))
