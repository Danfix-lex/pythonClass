def join_seperated_words_together(firstLetters, secondLetters):
    first_part = secondLetters[:2] + firstLetters[-1]
    second_part = firstLetters[:2] + secondLetters[-1]
    return first_part + " " + second_part