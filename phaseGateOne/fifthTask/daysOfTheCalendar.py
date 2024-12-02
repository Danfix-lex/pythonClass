dayNumber = int(input("Enter today's day: "))
futureDayNumber = int(input("input Future's day number: "))
sunday = 0
monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6

if dayNumber == 0 or dayNumber == 0 + 8 :
    dayName = "Sunday"
elif dayNumber == 1 or dayNumber == dayNumber + 8:
    dayName = "Monday"
elif dayNumber == 2 or dayNumber == dayNumber + 8:
    dayName = "Tuesday"
elif dayNumber == 3 or dayNumber == dayNumber + 8:
    dayName = "Wednesday"
elif dayNumber == 4 or dayNumber == dayNumber + 8:
    dayName = "Thursday"
elif dayNumber == 5 or dayNumber == dayNumber + 8:
    dayName = "Friday"
elif dayNumber == 6 or dayNumber == dayNumber + 8:
    dayName = "Saturday"
else:
    dayName = "Invalid input"

print(f"Today is {dayName}")
if futureDayNumber == sunday or futureDayNumber == sunday + 8:
    print(f"Today is {dayName} and the future's day is sunday")
elif futureDayNumber == monday or futureDayNumber == monday + 8:
    print(f"Today is {dayName} and the future day is monday")
elif futureDayNumber == tuesday or futureDayNumber == tuesday + 8:
    print(f"Today is {dayName} and the future day is tuesday")
elif futureDayNumber == wednesday or futureDayNumber == wednesday + 8:
    print(f"Today is {dayName} and the future day is wednesday")
elif futureDayNumber == thursday or futureDayNumber == thursday + 8:
    print(f"Today is {dayName} and the future day is thursday")
elif futureDayNumber == friday or futureDayNumber == friday + 8:
    print(f"Today is {dayName} and the future day is friday")
elif futureDayNumber == saturday or futureDayNumber == saturday + 8:
    print(f"Today is {dayName} and the future day is saturday")
else:
    print("The future Day you entered is out a range for the days in the current week, please start again and enter the day number of the current week")

