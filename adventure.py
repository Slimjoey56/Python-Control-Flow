#Advanced While Loop Techniques: Practical Applications and Considerations
available_exit = ["north","south","east","west"]

chosen_exit = ""

while chosen_exit not in available_exit:
    chosen_exit =  input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break

else:
    print("arent u glad u got out of there")
