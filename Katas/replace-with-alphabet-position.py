def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    position = []
    for char in text:
        count = 0
        for i in alphabet:
            count += 1
            if i == char or i.upper() == char:
                position.append(str(count))
    final = ' '.join(position)
    return final
    pass
