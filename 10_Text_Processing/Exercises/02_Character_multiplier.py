data = input().split()

total_sum = 0

if len(data[0]) > len(data[1]):
    index = 0
    for char in data[0]:
        if index < len(data[1]):
            total_sum += ord(char) * ord(data[1][index])
            index += 1

    for char in data[0][len(data[1]):]:
        total_sum += ord(char)
elif len(data[0]) < len(data[1]):
    index = 0
    for char in data[1]:
        if index < len(data[0]):
            total_sum += ord(char) * ord(data[0][index])
            index += 1

    for char in data[1][len(data[0]):]:
        total_sum += ord(char)
else:
    for index in range(len(data[0])):
        total_sum += ord(data[0][index]) * ord(data[1][index])

print(total_sum)