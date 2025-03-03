def get_letters_inside_word(word, letter):
    if len(word[:3]) == len(word[-3:]):
        double_letter = word[:3] + letter + word[-3:]
    else:
        double_letter = word + letter
    return double_letter