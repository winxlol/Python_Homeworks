year = int(input())

happy_year = ""

while len(happy_year) != 4:
    year += 1
    year = str(year)
    for num in year:
        if num in happy_year:
            happy_year = ""
            year = int(year)
            break
        else:
            happy_year += num
            year = int(year)

print(happy_year)
