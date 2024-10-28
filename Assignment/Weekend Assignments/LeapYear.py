year = int(input("Enter Year number: "))
leapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if leapYear:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

