given_attempt = int(input())

total_sum = 0

for current_attempt in range(given_attempt):
    current_char = input()
    total_sum += ord(current_char)

print(f"The sum equals: {total_sum}")
