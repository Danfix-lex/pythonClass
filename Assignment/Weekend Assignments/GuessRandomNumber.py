answer = 10
guess = None

while guess != answer:
    guess = int(input("Guess the number between 1 and 10: "))

    if guess > answer:
        print("Too high, try again.")
    elif guess < answer:
        print("Too low, try again.")

print("Congratulations! You guessed it right!!!")

