import random, time, sys

print("Welcome to the 'Guess the Number' game!")

name = input("What is your name? ")

print("Hello there, " + str(name) + ". Welcome to the number guessing game!")

min = int(input("What is the minumum number you would like to guess your number from? "))

time.sleep(1)

max = int(input("What is the maximum number you would like to guess your number from? "))

print("Generating number... ")

time.sleep(1)

generatedNumber = random.randint(min, max)

print("Number generated!")

tries = 5 

time.sleep(1)

print(str(name) + ", you have " + str(tries) + " tries to guess the number.") 

while tries > 0:
    userNumber = int(input("What is your guess for the number? "))

    if userNumber == generatedNumber:
        print("You won, " + str(name) + "!")
        print("You did it in " + str(tries) + " tries! Great job, " + str(name) + "!") 
        print("Thanks for playing, " + str(name) + "! Have a good day/night!")
        sys.exit()
    elif userNumber > generatedNumber:
        print("You are too high.")
        tries = tries - 1
        print("You have " + str(tries) + " tries left!")
    elif userNumber < generatedNumber:
        print("You are too low.")
        tries = tries - 1
        print("You have " + str(tries) + " tries left!")

if tries == 0:
        print("You lose! Good try though! The number was " + str(generatedNumber) + "!")
        print("Thanks for playing, " + str(name) + "! Have a good day/night!")
        sys.exit()
 

