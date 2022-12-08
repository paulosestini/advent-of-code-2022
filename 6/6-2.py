with open('./6/input.txt') as file:
    signal = file.read().strip()
    marker_chars = []

    i = 0
    while len(marker_chars) != 14:
        next_char = signal[i]
        if next_char in marker_chars:
            char_position = marker_chars.index(next_char)
            marker_chars = marker_chars[char_position+1:]

        marker_chars.append(next_char)
        i += 1

    print(i)
