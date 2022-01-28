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

welcome()