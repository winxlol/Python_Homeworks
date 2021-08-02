dwarfs = {}

while True:
    data = input()

    if data == "Once upon a time":
        break

    dwarf_details = data.split(" <:> ")

    name = dwarf_details[0]
    hat_color = dwarf_details[1]
    power = int(dwarf_details[2])

    if hat_color not in dwarfs:
        dwarfs[hat_color] = {}

    if name not in dwarfs[hat_color]:
        dwarfs[hat_color][name] = power
    else:
        if power > dwarfs[hat_color][name]:
            dwarfs[hat_color][name] = power

sorted_Mydict = sorted(dwarfs.items(), key=lambda x: -len(x[1].values()))
pairs = [(color, name, power) for color, inner in sorted_Mydict for name, power in inner.items()]
[print(f"({color}) {name} <-> {power}") for color, name, power in sorted(pairs, key=lambda x: -x[2])]
