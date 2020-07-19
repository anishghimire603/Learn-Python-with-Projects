import re

print("Our logical Calulator")
print("Type 'quit' to Exit.\n")

previous = 0                                                     #variables
run = True

def perform_math():                                              #defining function
    global run
    global previous                                              #acessing variables
    equation = ""

    if previous == 0:                                             #using conditional statment
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == "quit":
        print("Bye Bye")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()""]', '', equation)

    if previous == 0:

        previous = eval(equation)                                    #for math operation.
    else:
        previous = eval(str(previous) + equation)

   # print("You Typed", previous)

while run:
    perform_math()