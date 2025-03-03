def calculate_letters_frequency_and_appearance(letters):
    frequency = {}
    for char in letters:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency