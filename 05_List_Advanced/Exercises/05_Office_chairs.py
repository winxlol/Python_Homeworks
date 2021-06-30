rooms = int(input())

free_chairs = 0
is_every_room_left_chair = True

for room in range(1, rooms + 1):
    room_information = input().split()

    chairs = room_information[0]
    visitors = int(room_information[1])

    if visitors > len(chairs):
        chairs_needed = visitors - len(chairs)
        print(f"{chairs_needed} more chairs needed in room {room}")
        is_every_room_left_chair = False
    else:
        free_chairs += len(chairs) - visitors

if is_every_room_left_chair:
    print(f"Game On, {free_chairs} free chairs left")
