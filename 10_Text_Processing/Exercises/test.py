number = int(input())

for i in range(number):
    data = input()

    start_index_name = data.index("@")
    end_index_name = data.index("|")

    start_index_age = data.index("#")
    end_index_age = data.index("*")

    name = data[start_index_name + 1:end_index_name]
    age = data[start_index_age + 1:end_index_age]

    print(f"{name} is {age} years old.")