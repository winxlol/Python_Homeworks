day_events = input().split("|")

initial_energy = 100
initial_coins = 100

current_energy = 0

is_day_completed = True

for day_event in day_events:
    current_event = day_event.split("-")
    event = current_event[0]
    value = int(current_event[1])

    if event == "rest":
        temp_energy = initial_energy
        initial_energy += value
        if initial_energy > 100:
            initial_energy = 100
            current_gained_energy = 100 - temp_energy
            print(f"You gained {current_gained_energy} energy.")
            print(f"Current energy: {initial_energy}.")
        else:
            print(f"You gained {value} energy.")
            print(f"Current energy: {initial_energy}.")
    elif event == "order":
        if initial_energy >= 30:
            initial_coins += value
            initial_energy -= 30
            print(f"You earned {value} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
            continue
    else:

        if initial_coins > value:
            initial_coins -= value
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            is_day_completed = False
            break


if is_day_completed:
    print(f"Day completed!\nCoins: {initial_coins}\nEnergy: {initial_energy}")

