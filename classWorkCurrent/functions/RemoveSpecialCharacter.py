def get_special_characters_away(word):
    current_special_characters = ""
    for letter in word:
        if letter.isalpha():
            current_special_characters += letter
    return current_special_characters