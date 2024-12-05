#def get_number_plus_list(numbers):
#    return [i + i for i in numbers]
#numbers = [1, 2, 3]
#print(get_number_plus_list(numbers))


#def get_words_length_with_number(list_words, number):
#   return [i for i in list_words if len(i) >= number]

def get_total_whole_number(numbers):
    return sum([int(x) for x in str(numbers)])
    
def get_all_vowel_letters_out_of_words(message):
    return [i for i in message if i in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"] (i = message.remove())]




#def guy(num):
#    return[list(lambda x: (x*x for x in range(num)), num)]
    
#numbers = 4
#print(square_numbers)

