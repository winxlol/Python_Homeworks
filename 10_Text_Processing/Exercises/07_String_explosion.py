data = input()

explosion = 0
string_result = ""


for i in range(len(data)):

    if data[i] == ">":
        explosion += int(data[i + 1])
        string_result += ">"
    else:
        if explosion == 0:
            string_result += data[i]
        else:
            if i < len(data):
                explosion -= 1

print(string_result)
