def odd_and_even_list(numberList)
    oddAndEvenList = []
    even = True
    odd = False
    for i in range(len(numberList)):
        if numberList[i] % 2 == 0:
            oddAndEvenList.append(even)
        else:
            oddAndEvenList.append(odd)
    print(oddAndEvenList)
