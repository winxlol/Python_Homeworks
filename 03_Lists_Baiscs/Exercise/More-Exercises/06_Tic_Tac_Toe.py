FIRST_PLAYER = 1
SECOND_PLAYER = 2

first_row = list(map(int, input().split()))
second_row = list(map(int, input().split()))
third_row = list(map(int, input().split()))

while True:

    # THIS CHECK IS FOR FIRST PLAYER

    if (
            first_row[0] == FIRST_PLAYER and first_row[1] == FIRST_PLAYER and first_row[2] == FIRST_PLAYER
            or second_row[0] == FIRST_PLAYER and second_row[1] == FIRST_PLAYER and second_row[2] == FIRST_PLAYER
            or third_row[0] == FIRST_PLAYER and third_row[1] == FIRST_PLAYER and third_row[2] == FIRST_PLAYER
            or first_row[0] == FIRST_PLAYER and second_row[0] == FIRST_PLAYER and third_row[0] == FIRST_PLAYER
            or first_row[1] == FIRST_PLAYER and second_row[1] == FIRST_PLAYER and third_row[1] == FIRST_PLAYER
            or first_row[2] == FIRST_PLAYER and second_row[2] == FIRST_PLAYER and third_row[2] == FIRST_PLAYER
            or first_row[0] == FIRST_PLAYER and second_row[1] == FIRST_PLAYER and third_row[2] == FIRST_PLAYER
            or first_row[2] == FIRST_PLAYER and second_row[1] == FIRST_PLAYER and third_row[0] == FIRST_PLAYER
    ):
        print("First player won")
        break

    # THIS CHECK IS FOR SECOND PLAYER

    elif (
            first_row[0] == SECOND_PLAYER and first_row[1] == SECOND_PLAYER and first_row[2] == SECOND_PLAYER
            or second_row[0] == SECOND_PLAYER and second_row[1] == SECOND_PLAYER and second_row[2] == SECOND_PLAYER
            or third_row[0] == SECOND_PLAYER and third_row[1] == SECOND_PLAYER and third_row[2] == SECOND_PLAYER
            or first_row[0] == SECOND_PLAYER and second_row[0] == SECOND_PLAYER and third_row[0] == SECOND_PLAYER
            or first_row[1] == SECOND_PLAYER and second_row[1] == SECOND_PLAYER and third_row[1] == SECOND_PLAYER
            or first_row[2] == SECOND_PLAYER and second_row[2] == SECOND_PLAYER and third_row[2] == SECOND_PLAYER
            or first_row[0] == SECOND_PLAYER and second_row[1] == SECOND_PLAYER and third_row[2] == SECOND_PLAYER
            or first_row[2] == SECOND_PLAYER and second_row[1] == SECOND_PLAYER and third_row[0] == SECOND_PLAYER
    ):
        print("Second player won")
        break

    else:
        print("Draw!")
        break
