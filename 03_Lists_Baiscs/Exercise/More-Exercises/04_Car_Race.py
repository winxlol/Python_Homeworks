list_numbers = list(map(int, input().split()))

laps = len(list_numbers) // 2

first_car_count = 0
second_car_count = 0

index = 0

for current_lap in list_numbers:
    if index == laps:
        index = 0
        break
    first_car_count += current_lap
    if current_lap == 0:
        first_car_count = first_car_count * 0.8
    index += 1

list_numbers.reverse()

for current_lap in list_numbers:
    if index == laps:
        index = 0
        break
    second_car_count += current_lap
    if current_lap == 0:
        second_car_count = second_car_count * 0.8
    index += 1

list_numbers.reverse()

if first_car_count > second_car_count:

    print(f"The winner is right with total time: {second_car_count:.1f}")
else:

    print(f"The winner is left with total time: {first_car_count:.1f}")
