attempt = 0
secret_number = 7
while True:
    guess = int(input("guess a number: "))
    attempt += 1
    if guess == secret_number:
        print( "you guessed it" )
        print( "attempts: ", attempt )
        break
    elif guess < secret_number:
        print( "too low" )
        print( "attempts: ", attempt )
    else:
        print( "too high" )
        print( "attempts: ", attempt )    

