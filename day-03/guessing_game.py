while True:
    guess = int(input("Guess a number: "))

    if guess == 7:
        print("You guessed it!")
        break
    elif guess < 7:
        print("Too low!")
    else:
        print("Too high!")
