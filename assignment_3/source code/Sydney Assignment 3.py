#Sydney Timmons
#Assignment 3 Comp Sci 101L
import random
play="y"
while play == "y":
    print("Welcome to the Flarsheim Guesser!")
    print("Please think of a number between and including 1 and 100.")
    number= int(input("What is the remainder when your number is divided by 3?"))
    if number < 0:
        print("The value entered must be 0 of greater.")
        number= int(input("What is the remainder when your number is divided by 3?"))
    elif number > 2:
        print("The value entered must be less than 3.")
        number= int(input("What is the remainder when your number is divided by 3?"))
    else:
        pass
    number1= int(input("What is the remainder when your number is divided by 5?"))
    number2= int(input("What is the remainder when your number is divided by 7?"))
    print("How amazing is that?")
    play=str(input("Do you want to play again? y or n"))
    
        


