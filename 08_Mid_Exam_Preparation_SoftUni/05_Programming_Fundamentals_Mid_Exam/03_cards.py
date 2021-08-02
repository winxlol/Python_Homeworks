def cards_not_exist(card):
    if card not in cards:
        return False


def add(card_name):
    if cards_not_exist(card_name) is False:
        return print("Card not found.")

    new_deck.append(card_name)


def insert(card_name, index):
    if cards_not_exist(card_name) is False or index > len(new_deck) or index < 0:
        return print("Error!")

    new_deck.insert(index, card_name)


def remove(card_name):
    if card_name not in new_deck:
        return print("Card not found.")

    new_deck.remove(card_name)


def swap(card_name_one, card_name_two):
    card_one_index = new_deck.index(card_name_one)
    card_two_index = new_deck.index(card_name_two)

    new_deck[card_one_index], new_deck[card_two_index] = new_deck[card_two_index], new_deck[card_one_index]


cards = input().split(":")
new_deck = []

if len(cards) > 0:
    while True:
        tokens = input()

        if tokens == "Ready":
            break

        commands = tokens.split()

        move = commands[0]

        if move == "Add":
            card_name = commands[1]

            add(card_name)
        elif move == "Insert":
            card_name = commands[1]
            index = int(commands[2])

            insert(card_name, index)
        elif move == "Remove":
            card_name = commands[1]

            remove(card_name)
        elif move == "Swap":
            card_name_one = commands[1]
            card_name_two = commands[2]

            swap(card_name_one, card_name_two)

        if tokens == "Shuffle deck":
            new_deck = new_deck[::-1]

    print(" ".join(new_deck))
