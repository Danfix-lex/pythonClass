alphabet = input()
if len(alphabet) != 1:
    print("Error: Please enter a single character.")
else:
    letter = input_char[0]
    if letter.isalpha():
        if letter in 'aeiouAEIOU':
            print("Input letter is Vowel")
        else:
            print("Input letter is Consonant")
