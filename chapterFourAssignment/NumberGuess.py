number = 456
for i in range(0, 1000):
    guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
    if guess > number:
        print("Too high. Try again")
    elif guess < number:
        print("Too low. Try again")
    else:
        print("Congratulations. You guessed the number!")
        break
    continuation = int(input("Do you want to continue? Type 0 for no or 1 for yes: "))
    if continuation == 0:
        break

