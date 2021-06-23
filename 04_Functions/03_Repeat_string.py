#def repeat_string(data, counter):
#    return list(map(lambda x: x * counter, data))


#data = input().split()
#counter = int(input())
#print("".join(repeat_string(data, counter)))


def repeat_string(data, counter):
    result = lambda a, b: a * b
    return result


data = input()
counter = int(input())
print(repeat_string(data, counter))

