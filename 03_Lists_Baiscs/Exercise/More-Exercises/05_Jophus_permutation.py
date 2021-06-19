elements = input().split()
k = int(input())

index = 0

removed_elements = []

while not len(elements) == 0:

    if not index + 1 == k:
        elements.append(elements[0])
        elements.pop(0)
    else:
        removed_elements.append(elements[0])
        elements.pop(0)
        index = 0
        continue

    index += 1


print(str(removed_elements).replace(" ", "").replace("\'", ""))