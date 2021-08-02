biscuits = input().split(", ")

while True:
    tokens = input()

    if tokens == "No More Money":
        break

    command = tokens.split()

    if command[0] == "OutOfStock":
        biscuit = command[1]
        while biscuit in biscuits:
            biscuit_index = biscuits.index(biscuit)
            biscuits[biscuit_index] = "None"
    elif command[0] == "Required":
        biscuit = command[1]
        index = int(command[2])

        if 0 <= index < len(biscuits) and biscuits[index] != "None":
            biscuits[index] = biscuit
    elif command[0] == "Last":
        biscuit = command[1]

        biscuits.append(biscuit)

result = [el for el in biscuits if el != "None"]
print(" ".join(result))

