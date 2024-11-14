def get_product(*args):
    result = 1
    for num in args:
        result = result * num
    return result
    
print(get_product(2, 3, 4))        
print(get_product(5, 10))         
print(get_product(7))             
print(get_product(1, 2, 3, 4, 5)) 

