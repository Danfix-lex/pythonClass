DeadlinePlanDayCheck = int(input("Enter the number of days you took the book: "))

if DeadlinePlanDayCheck > 30:
    print("Your membership has been cancelled.")
else:
    if DeadlinePlanDayCheck > 10:
        print("The fine is 5 rupees.")
    else:
        if DeadlinePlanDayCheck >= 6:
            print("The fine is 1 rupee.")
        else:
            if DeadlinePlanDayCheck >= 1:
                print("The fine is 50 Paise.")
            else:
                print("No fine. The book is returned on time.")

