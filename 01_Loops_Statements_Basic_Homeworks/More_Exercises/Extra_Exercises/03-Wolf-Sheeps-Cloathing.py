animals = input().split(", ")
index = 0

while True:
    if "wolf" == animals[-1]:
        print("Please go away and stop eating my sheep")
        break
    else:
        for sheep in reversed(animals):
            index += 1
            if sheep != "sheep":
                print(f"Oi! Sheep number {index - 1}! You are about to be eaten by a wolf!")
                break
        break
