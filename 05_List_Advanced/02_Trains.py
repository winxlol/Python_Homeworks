def add(people, train_wagons):
    train_wagons[-1] += people


def insert(index, people, train_wagons):
    train_wagons[index] += people


def leave(index, people, train_wagons):
    train_wagons[index] -= people


wagons = int(input())

train_wagons = []

for wagon in range(wagons):
    train_wagons.append(0)

while True:
    data = input().split()

    command = data[0]

    if command == "End":
        print(train_wagons)
        break

    if command == "add":
        people = int(data[1])

        add(people, train_wagons)
    elif command == "insert":
        index = int(data[1])
        people = int(data[2])

        insert(index, people, train_wagons)
    elif command == "leave":
        index = int(data[1])
        people = int(data[2])

        leave(index, people, train_wagons)
