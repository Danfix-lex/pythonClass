def get_cipher_encryption_key(text):
    encryption = ""
    shift = 13
    for a in text:
        if a.isalpha():
            if a.islower():
                base = 'a'
            else:
                base = 'A'
            result = chr((ord(a) - ord(base) + shift) % 26 + ord(base))
            encryption += result
        else:
            encryption += a
    return encryption



# sudo code
# declear a variable and assign to an empty string
# declear a variable of int and assign to 13
# loop into the text using a for loop
# check if each text is a letter, if yes declear a variable called base and assign to a char a is the letter
# is a small letter or assign it to char A is the letter is a capital letter
# calculated it as the letter - the base + the number of shifts % the number of the alphabets + the base
# store it in the result variable
#if no the store it directly in the result variable

