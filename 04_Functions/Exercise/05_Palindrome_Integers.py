def palindrome_numbers(collection: list):

    for element in collection:
        reverse_element = list(reversed(element))
        joined_element = "".join(reverse_element)
        cast_to_int = int(joined_element)

        if cast_to_int == int(element):
            print("True")
        else:
            print("False")


data = input().split(", ")
palindrome_numbers(data)
