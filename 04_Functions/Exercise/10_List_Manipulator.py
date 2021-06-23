import sys


def exchange(data, index):
    if 0 <= index < len(data):
        for current_index in range(index + 1):
            data.append(data.pop(0))
        return data
    else:
        print("Invalid index")


def max_even_or_odd(data, extra_event):
    max_even_number = -sys.maxsize
    index_even_number = -1
    max_odd_number = -sys.maxsize
    index_odd_number = -1

    for index in range(len(data)):
        if data[index] % 2 == 0:
            if data[index] >= max_even_number:
                max_even_number = data[index]
                index_even_number = index

        else:
            if data[index] >= max_odd_number:
                max_odd_number = data[index]
                index_odd_number = index

    if extra_event == "even":
        if index_even_number >= 0:
            return index_even_number
        else:
            return "No matches"
    elif extra_event == "odd":
        if index_odd_number >= 0:
            return index_odd_number
        else:
            return "No matches"


def min_even_or_odd(data, extra_event):
    min_even_number = sys.maxsize
    index_even_number = -1
    min_odd_number = sys.maxsize
    index_odd_number = -1

    for index in range(len(data)):
        if data[index] == 0:
            continue
        if data[index] % 2 == 0:
            if data[index] <= min_even_number:
                min_even_number = data[index]
                index_even_number = index

        else:
            if data[index] <= min_odd_number:
                min_odd_number = data[index]
                index_odd_number = index

    if extra_event == "even":
        if index_even_number >= 0:
            return index_even_number
        else:
            return "No matches"
    elif extra_event == "odd":
        if index_odd_number >= 0:
            return index_odd_number
        else:
            return "No matches"


def first_even_odd(data, event, index, operation):
    first_list_numbers = []
    if index > len(data):
        return "Invalid count"

    count = 0

    if operation == "even":
        for number in data:
            if number == 0:
                first_list_numbers = []
                return first_list_numbers
            if number % 2 == 0:
                first_list_numbers.append(number)
                count += 1
                if count == index:
                    return first_list_numbers
    elif operation == "odd":
        for number in data:
            if number == 0:
                first_list_numbers = []
                return first_list_numbers
            if number % 2 == 1:
                first_list_numbers.append(number)
                count += 1
                if count == index:
                    return first_list_numbers

    return first_list_numbers


def last_even_odd(data, event, index, operation):
    last_list_numbers = []
    if index > len(data):
        return "Invalid count"

    count = 0

    if operation == "even":
        for number in reversed(data):
            if number == 0:
                first_list_numbers = []
                return first_list_numbers
            if number % 2 == 0:
                last_list_numbers.append(number)
                count += 1
                if count == index:
                    return list(reversed(last_list_numbers))
    elif operation == "odd":
        for number in reversed(data):
            if number == 0:
                first_list_numbers = []
                return first_list_numbers
            if number % 2 == 1:
                last_list_numbers.append(number)
                count += 1
                if count == index:
                    return list(reversed(last_list_numbers))

    return list(reversed(last_list_numbers))


data = list(map(int, input().split()))

while True:
    command = input().split()

    if command[0] == "end":
        print(data)
        break
    event = command[0]

    if event == "exchange":
        index = int(command[1])
        exchange(data, index)
    elif event == "max":
        extra_event = command[1]

        print(max_even_or_odd(data, extra_event))
    elif event == "min":
        extra_event = command[1]

        print(min_even_or_odd(data, extra_event))
    elif event == "first":
        index = int(command[1])
        operation = command[2]

        print(first_even_odd(data, event, index, operation))
    elif event == "last":
        index = int(command[1])
        operation = command[2]

        print(last_even_odd(data, event, index, operation))

