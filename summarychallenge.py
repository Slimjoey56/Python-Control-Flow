print("Please choose your option from the below list")
print("1:\tLearn Python")
print("2:\tLearn Java")
print("3:\tGo Swimming")
print("4:\tHave Dinner")
print("5:\tGo to bed")
print("0:\tExit")

while True:
    choice =input()

    if choice =="0":
        break
    elif choice in "1,2,3,4,5":
        print("You chose {}".format(choice))

    else:
     print("Please choose your option from the below list")
    print("1:\tLearn Python")
    print("2:\tLearn Java")
    print("3:\tGo Swimming")
    print("4:\tHave Dinner")
    print("5:\tGo to bed")
    print("0:\tExit")
