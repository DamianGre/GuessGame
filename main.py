import random

again = True
print("It's a number guessing game. Cpu will pick random number from range 0-100, to win You must pick same number as cpu. \nIf You want to end game during game enter 'quit' instead of number")
while again:
    triesCounter=0
    cpuRandom = random.randint(1, 100)
    userNumber = ""
    while userNumber != cpuRandom:
        userNumber = input("Enter number:  ")
        while userNumber.isdigit() == False:
            if userNumber.lower() == "quit":
                again = False
                print("End of the game.")
                break
            print("You have entered wrong data, insert digits")
            userNumber = input("Enter number: ")
        if userNumber.lower() == "quit":
            break
        if userNumber.lower() != "quit":
            userNumber = int(userNumber)
            if userNumber < cpuRandom:
                print("Your number is LOWER then cpu number")
                triesCounter+=1
            elif userNumber > cpuRandom:
                print("Your number is HIGHER then cpu number")
                triesCounter += 1
            else:
                print("WINNER! Your number is same as cpu number! CONGRATULATIONS")
                print("Your tries counter = " + str(triesCounter))
    if str(userNumber).lower() != "quit":
        playAgain = input("Do You want to play again? yes/no ")
        if(playAgain.lower() == "no"):
            again = False
            print("End of the game.")
        print("New Game has started")