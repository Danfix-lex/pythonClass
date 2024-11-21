def get_acronym(text):
    return ''.join(word[0].upper() for word in text.split())

text = "Portable Network Graphics"
result = get_acronym(text)
print(result)

