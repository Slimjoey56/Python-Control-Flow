import random

highest = 1000
answer = random.randint(1,highest)
print(answer) #TODO remove after testing
guess = 0 #initialize to any number that does not equals the  answer
print("Please guess a number between 1 and {}: ".format(highest))
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("well done you guessed it  ")
        break
    else:

        if guess < answer:
            print("Please guess higher")
        else:#guess must b greater than answer
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("well done you guessed it  ")
        # else:
        #     print("sorry,you have not guessed correctly")
