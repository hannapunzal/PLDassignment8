#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not Display ”Try again y/n” after each game
#If the user enter “y” the user will lottery again if “n” the program will exit.
# color palette: yellow [highlights;title] green [name;win], red [lost], blue [input]
import time 
import random

def welcome():
    global name
    name = input("\033[5;49;36mEnter player's name\33[0m: ")    
    print(f"\n\033[5;49;33mHey there,\33[0m \033[0;49;32m{name}\33[0m\033[5;49;33m!\33[0m \033[5;49;33mWelcome to HF's Merry Lottery!\33[0m") #green name, #yellow lottery title
    time.sleep(1)
    print("\n\033[5;49;33mGuess the 3 numbers (0-9) to win the jackpot!\33[0m") #yellow 
    time.sleep(3) 
    print("\n\033[5;49;36mLet's get you started!\33[0m")
    time.sleep(.5)

def lotteryGame():
    lotteryGame = True
    while lotteryGame:
        firstNumber = int(input("\n\033[5;49;36mEnter first number\33[0m: ")) #\n\033[5;49;36m closest shade
        secondNumber = int(input("\033[5;49;36mEntersecond number\33[0m: "))
        thirdNumber = int(input("\033[5;49;36mEnter third number\33[0m: "))

        systemFirstNum = random.randint(0,9)
        systemSecondNum = random.randint(0,9)
        systemThirdNum = random.randint(0,9)
    
        askLottery = firstNumber, secondNumber, thirdNumber
        systemNumber = (systemFirstNum, systemSecondNum, systemThirdNum)
        time.sleep(1.25)
        if  askLottery == systemFirstNum and systemSecondNum and systemThirdNum:
            print(f"\n[0;49;32mCongratulations, {name}! You got the jackpot! The Winning numbers are: {systemNumber}.")
        else:
            print(f"\n\033[5;49;31mSorry, {name}. You lost. The\33[0m \033[0;49;32mWinning Numbers\33[0m \033[5;49;31mare\33[0m:\n\033[0;49;32m{systemNumber}\33[0m")        
        time.sleep(2.5)
        askAnotherRound = input("\n\033[5;49;33mIf you wish to play again, enter '\33[0m\033[5;49;36my\33[0m\033[5;49;33m'. If not, enter '\33[0m\033[5;49;36mn\33[0m\033[5;49;33m'. Thank you!\33[0m\n").lower()
        while True:
            if askAnotherRound == "y":
                lotteryGame = True
                break
            elif askAnotherRound == "n":
                lotteryGame = False
                print(f"\033[5;49;36mThank you for playing HF's Merry Lottery!\33[0m")
                break

welcome()
lotteryGame()