def get_list_cube_total(numbers):
    cube_numbers = [] 
    for number in numbers:
        cube = number * number * number 
        cube_numbers.append(cube) 
    return cube_numbers 
