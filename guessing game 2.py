answer =  5
print("Please guess a number between 1 and 10: ")
guess = int(input())
if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("well done u guessed it ")
    else:
        print("sorry u guessed wrong")
elif guess > answer:
    print("Please guess lower ")
    guess = int(input())
    if guess  == answer:
        print("well done u guessed it")
    else:
        print("sorry u guessed wrong")
else:
    print("You got it first time")
