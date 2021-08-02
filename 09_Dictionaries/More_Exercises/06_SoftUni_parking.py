people = int(input())

registred_members = {}

for person in range(people):
    data = input().split()

    command = data[0]
    username = data[1]

    if command == "register":
        license_plate = data[2]

        if username not in registred_members:
            registred_members[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")

    elif command == "unregister":

        if username not in registred_members:
            print(f"ERROR: user {username} not found")
        else:
            registred_members.pop(username)
            print(f"{username} unregistered successfully")


for name, plate in registred_members.items():
    print(f"{name} => {plate}")