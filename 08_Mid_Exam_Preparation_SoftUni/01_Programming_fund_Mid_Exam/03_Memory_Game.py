def wrong_index_and_out_bounds(moves, index_one, index_two):
        middle_index = len(elements) // 2
        moves = str(moves)
        for _ in range(2):
            elements.insert(middle_index, f"-{moves}a")
        return print("Invalid input! Adding additional elements to the board")


def same_elements(index_one, index_two):
    if elements[index_one] == elements[index_two]:
        current_element = elements[index_one]
        if index_one > index_two:
            elements.pop(index_one)
            elements.pop(index_two)
        else:
            elements.pop(index_one)
            elements.pop(index_two - 1)
        return print(f"Congrats! You have found matching elements - {current_element}!")
    else:
        return print("Try again!")


elements = input().split()

moves = 0
is_all_hit = False

while True:
    tokens = input()

    if tokens == "end":
        break

    moves += 1

    indecies = tokens.split()

    index_one = int(indecies[0])
    index_two = int(indecies[1])

    if index_one == index_two or \
            index_one >= len(elements) or \
            index_one < 0 or \
            index_two < 0 or \
            index_two >= len(elements):
        wrong_index_and_out_bounds(moves, index_one, index_two)
        continue

    same_elements(index_one, index_two)

    if len(elements) == 0:
        is_all_hit = True
        print(f"You have won in {moves} turns!")
        break

if is_all_hit is False:
    print(f"Sorry you lose :(\n{' '.join(elements)}")
