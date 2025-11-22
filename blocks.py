#. Mastering if Statements: Controlling Program Flow with Conditional Logic
name =input("Please Enter your name: ")
age =int( input("How old are you {0}? ".format(name)))
print(age)

# if age>=18:
#     print("You are old enough to vote ")
#     print("Please put an X in the box")
# else:
#     print("Please comeback in {0} years".format(18-age))
if age < 18:
    print("Please comeback in {0} years".format(18-age))
elif age==900:
    print("Sorry,Yoda , You die in return of Jedi")
else:
    print("You are old enough to vote ")
    print("Please put an X in the box")
