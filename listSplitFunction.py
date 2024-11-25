def get_split_list(lst):
    midpoint = len(lst) // 2
    
    first_half = lst[:midpoint]
    second_half = lst[midpoint:]
    
    if len(first_half) == len(second_half):
        return(first_half, second_half)
    elif len(first_half) != len(second_half):
        return(first_half, second_half)
    else:
        raise TypeError

