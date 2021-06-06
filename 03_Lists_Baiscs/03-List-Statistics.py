attempts = int(input())

positive_numbers = []
negative_numbers = []

for attempt in range(attempts):
    current_number = int(input())
    if current_number >= 0:
        positive_numbers.append(current_number)
    else:
        negative_numbers.append(current_number)

count_positive_numbers = len(positive_numbers)
sum_negative_numbers = sum(negative_numbers)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {count_positive_numbers}. Sum of negatives: {sum_negative_numbers}")