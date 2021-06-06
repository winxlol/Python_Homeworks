tail = input()
body = input()
head = input()

body_parts_list = [tail, body, head]

body_parts_list[0], body_parts_list[2] = body_parts_list[2], body_parts_list[0]

print(body_parts_list)