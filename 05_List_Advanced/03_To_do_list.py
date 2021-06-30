todo_list = []

while True:
    todo_notes = input().split("-", maxsplit=1)
    if todo_notes[0] == "End":
        break

    priority = int(todo_notes[0])
    note = todo_notes[1]

    todo_list.append((priority, note))

comprehanse = [note for priority, note in sorted(todo_list)]

print(comprehanse)