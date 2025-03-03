def get_tuple_character_from_input(word, letter):
    tuple_count = 0
    for char in word:
        if char == letter:
            tuple_count += 1
    return letter, tuple_count