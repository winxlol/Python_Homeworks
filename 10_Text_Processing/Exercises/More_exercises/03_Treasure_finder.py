key = input().split()

key = [int(el) for el in key]

hidden_message = ""

while True:
    data = input()

    if data == "find":
        break

    index = 0

    for char in data:
        hidden_message += chr(ord(char) - key[index])

        index += 1

        if index == len(key):
            index = 0

    start_type_index = hidden_message.index("&")
    start_cordinates_index = hidden_message.index("<")
    end_cordinates_index = hidden_message.index(">")

    end_type_index = start_type_index

    while True:
        end_type_index += 1
        if hidden_message[end_type_index] == "&":
            break

    treasure = hidden_message[start_type_index + 1:end_type_index]
    cordinates = hidden_message[start_cordinates_index + 1:end_cordinates_index]

    print(f"Found {treasure} at {cordinates}")
    hidden_message = ""

