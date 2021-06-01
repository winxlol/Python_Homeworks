numbers = int(input())


for num in range(1, numbers + 1):
    string_num = str(num)
    if len(string_num) == 1:
        if num == 5 or num == 7:
            print(f"{num} -> True")
        else:
            print(f"{num} -> False")
    else:
        sum = 0
        sum += num // 10
        sum += num % 10
        if sum == 5 or sum == 7 or sum == 11:
            print(f"{num} -> True")
        else:
            print(f"{num} -> False")