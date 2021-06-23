def loading_bar(data):
    final_result = ""
    number_divided = data // 10

    for _ in range(number_divided):
        final_result += "%"

    number_empty_space = 10 - number_divided

    if number_empty_space < 10:
        for _ in range(number_empty_space):
            final_result += "."

    return final_result


data = int(input())
if data < 100:
    print(f"{data}% [{loading_bar(data)}]")
    print("Still loading...")
elif data == 100:
    print("100% Complete!")
    print(f"[{loading_bar(data)}]")