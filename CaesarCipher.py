def cesear_cipher(message, shift):
    translated = ''
    for x in message:
        if x != ' ':
            translated = translated + chr(ord(x) - shift)
        else:
            translated = translated + ' '
    return translated

message = 'Khoor wklv lv vhfuhw'
print(cesear_cipher(message, 3))

