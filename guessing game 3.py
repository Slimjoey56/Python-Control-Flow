answer =  5
print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You got it first time")

else:

    if guess < answer:
        print("Please guess higher")
    else:#guess must b greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("well done ")
    else:
        print("sorry,you have not guessed correctly")
