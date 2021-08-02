MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

data = input()

morse_word_translated = ""

current_morse_code = ""

for index, char in enumerate(data):
    if char == " ":
        for key, values in MORSE_CODE_DICT.items():
            if current_morse_code == values:
                morse_word_translated += key
                current_morse_code = ""
                break
    elif char == "|":
        morse_word_translated += " "
    else:
        current_morse_code += char

    if index + 1 == len(data):
        if char != " ":
            for key, values in MORSE_CODE_DICT.items():
                if current_morse_code == values:
                    morse_word_translated += key
                    current_morse_code = ""
                    break

print(morse_word_translated)

