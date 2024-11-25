def get_odd_and_even_list_number(numberList):
    oddAndEvenList = []
    even = True
    odd = False
    for i in range(len(numberList)):
        if numberList[i] % 2 == 0:
            oddAndEvenList.append(even)
        else:
            oddAndEvenList.append(odd)
    return(oddAndEvenList)
    raise TypeError
