citizenOne = input("Enter the name of the first citizen: ")
earningsOne = float(input("Enter " + citizenOne + "'s earnings: "))
taxOne = earningsOne * 0.15 if earningsOne <= 30000 else 30000 * 0.15 + (earningsOne - 30000) * 0.20
print("Total tax for", citizenOne + ":", taxOne)

citizenTwo = input("Enter the name of the second citizen: ")
earningsTwo = float(input("Enter " + citizenTwo + "'s earnings: "))
taxTwo = earningsTwo * 0.15 if earningsTwo <= 30000 else 30000 * 0.15 + (earningsTwo - 30000) * 0.20
print("Total tax for", citizenTwo + ":", taxTwo)

citizenThree = input("Enter the name of the third citizen: ")
earningsThree = float(input("Enter " + citizenThree + "'s earnings: "))
taxThree = earningsThree * 0.15 if earningsThree <= 30000 else 30000 * 0.15 + (earningsThree - 30000) * 0.20
print("Total tax for", citizenThree + ":", taxThree)

