MIN_NUMBER = 1
MAX_NUMBER = 100

while True:
    current_number = float(input())
    if 1 <= current_number <= 100:
        print(f"The number {current_number} is between {MIN_NUMBER} and {MAX_NUMBER}")
        break