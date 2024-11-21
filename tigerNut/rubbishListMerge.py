def get_list_number_merge(list_numbers):
    list_merge = []
    list1, list2 = list_numbers
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list_merge.append(list1[i])
            i += 1
        else:
            list_merge.append(list2[j])
            j += 1
    list_merge.extend(list1[i:])
    list_merge.extend(list2[j:])
    list_merge.sort()

    return list_merge
    raise TypeError  

list_numbers = ([1, 3, 5], [2, 4, 6])
list_merge = get_list_number_merge(list_numbers)
print(list_merge)

