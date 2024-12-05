#def get_numbers_from_letter(word):
#    return list(map(lambda x:int(x), filter(lambda x:x.isdigit(), word



my_dictionary = {"name":"Alice", "age":25, "city":"New York"}
print(my_dictionary)


my_dictionary = {"name":["Daniel","Olumide", "Samuel" ], "age":[20, 40, 50], "city":"New York"}
print(my_dictionary["name"][0], my_dictionary["age"][0])

my_dictionary = {"name":["Daniel","Olumide", "Samuel" ], "age":[20, 40, 50], "city":"New York"}
#for i in my_dictionary:
#    print(i)
#    if my_dictionary["name"][0] == "Daniel":
#        print(f"{my_dictionary["name"][0]} is among the list.")
#    else:
#        print ("Daniel is not on list")
#    break
#for j in my_dictionary.values():
#    print(j)

#for j, i in my_dictionary.items():

#    print(f"{i}: {j}")



#even = {x:x**2 for x in range(1, 10)}
#for j, i in even.items():
#    if i % 2 == 0:
#
        
def get_dictionary_list(keys, values):
    my_life = {}
    for i, j in zip(keys, values):
        my_life[i]=j
    return my_life

def get_values_from_dictionary(dictionary_values):
    return ([m for m in dictionary_values.values()])
    


my_dict = {"name":"Alice", "age":25}
new_data = {"city":"New York"}


nested_dict = {"person1":{"name":"Alice", "age":25},
                "person2":{"name": "Bob", "age":30}
                }
nested_dict["person1"]["city"]="New York"
print(nested_dict)
