data = input()

cipher = [chr(ord(char) + 3)for char in data]

print("".join(cipher))