key = int(input())
input_lines = int(input())

decrypted_message = []

for line in range(input_lines):
    current_char = input()
    current_char = chr(ord(current_char) + key)
    decrypted_message.append(current_char)

print("".join(decrypted_message))