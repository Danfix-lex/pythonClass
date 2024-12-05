def get_list_sum_total(numbers):
    total = 0 
    for number in numbers:
        total += number  
    return total 
    
def get_list_cube_total(numbers):
    cube_numbers = [] 
    for number in numbers:
        cube = number * number * number 
        cube_numbers.append(cube) 
    return cube_numbers 

def get_sum(sum_list):
    return get_list_sum_total([x for x in sum_list])

i = [1,3,5,6,8,9]

print(get_sum(i))

def get_cube(cube_list):
    return get_list_cube_total([j for j in cube_list])
    
m = [1,2,3,4,5]

print(get_cube(m))

