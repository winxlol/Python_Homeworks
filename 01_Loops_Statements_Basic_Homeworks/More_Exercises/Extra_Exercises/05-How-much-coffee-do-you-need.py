list_of_events = ['coding', 'dog', 'cat', 'movie']

coffee = 0

while True:
    command = input()
    if command == "END":
        break

    if command.lower() in list_of_events:
        if command.isupper():
            coffee += 2
        else:
            coffee += 1

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
