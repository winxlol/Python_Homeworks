lines = int(input())

list_brackets = []
is_balanced = False

for line in range(lines):
    current_data = input()

    if current_data == "(":
        list_brackets.append(current_data)

    if current_data == ")":
        list_brackets.append(current_data)

for bracket in range(len(list_brackets)):
    if bracket % 2 == 0:
        if list_brackets[bracket] == '(':
            is_balanced = True
        else:
            is_balanced = False
            print("UNBALANCED")
            break
    else:
        if list_brackets[bracket] == ')':
            is_balanced = True
        else:
            is_balanced = False
            print("UNBALANCED")
            break


if is_balanced:
    print("BALANCED")
