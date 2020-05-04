def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    #return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
    decoded = []
    split = morse_code.split(' ')
    for i in split:
        if i == '':
            decoded.append(' ')
        else:
            decoded.append(MORSE_CODE[i])
    decodedString = ''.join(decoded)
    newsplit =decodedString.split()
    decodedString = ' '.join(newsplit)
    return decodedString
