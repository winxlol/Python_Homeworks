def sequence_of_ascii_chars(start_index, end_index):
    start = ord(start_index)
    end = ord(end_index)

    list_of_sequence_chars = []

    for current_index in range(start + 1, end):
        current_index = chr(current_index)
        list_of_sequence_chars.append(current_index)

    return list_of_sequence_chars


first_string = input()
second_string = input()

print(" ".join(sequence_of_ascii_chars(first_string, second_string)))