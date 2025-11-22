#Using 'in' and 'not in' Operators for Efficient Python String Searching
parrot= "Norwegian Blue"

letter = input("Enter a Character: ")

if letter in parrot:
    print("{} is in {} ".format(letter,parrot))
else:
    print("I dont need that later")
