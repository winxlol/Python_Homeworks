data = list(map(int, input().split(".")))

n1 = data[0]
n2 = data[1]
n3 = data[2]

n3 += 1

if n3 > 9:
    n3 = 0
    n2 += 1
    if n2 > 9:
        n2 = 0
        n1 += 1

print(f"{n1}.{n2}.{n3}")
