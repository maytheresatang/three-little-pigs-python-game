
###########################################################################
##                                                                         #
##! /usr/bin/env python3                                                   #
## Prorgammed by: May Tang                                                 #
## Christmas 2019                                                          #
## Program Desciption: A text adventure game about the three little pigs   #
##                                                                         #
###########################################################################


##################################################################################
# --------------------------------------------------------------------------------#
# STORY
#    You are the wolf who is trying to blow the houses of three unfortunate pigs.
# --------------------------------------------------------------------------------#
##################################################################################

#IMPORT STATEMENTS
import time

# GET USER DATA
yourname = input("Please enter your name: ")
print("Welcome " + yourname+"!")

time.sleep(2)

# STORY DIALOG
# Introduction to the game
print(
    "In this game, there are three little pigs.\n\n"
    "The youngest pig, Rupert, has a house made of straw.\n"
    "The middle pig, Oscar, has a house made of wood.\n"
    "The oldest pig, Wilbur, has a house made of brick.\n\n"
    "You are the wolf. For some inexplicable reason, you want to blow all their houses down.\n"
    "You will need to choose how hard you want to blow down these houses.\n"
    "The sturdier houses are, the harder you will need to blow.\n"
    "Once you have blown down all three houses, the game will end. \n\n"
    "Good luck!\n")

time.sleep(2)

# MAIN FUNCTIONS

houses_blown = 0
whose_house = []
# A function to check which house the player wants to blow down
while houses_blown >= 0 and houses_blown < 3:
    if houses_blown == 0:
        house = input("Which pig's house would you like to blow down?\n(a) Rupert (Straw)\n(b) Oscar (Wood) \n(c) Wilbur (Brick)\n\nEnter your answer:")
    elif houses_blown > 0:
        house = input ("Whose house would you like to blow down next?\n(a) Rupert (Straw)\n(b) Oscar (Wood) \n(c) Wilbur (Brick)\n\nEnter your answer:")
    for letter in house:
        if letter == 'a':
            print(yourname +" you have chosen Rupert's straw house!\n")
    for letter in house:
        if letter == 'b':
            print(yourname +" you have chosen Oscar's wood house!\n")
    for letter in house:
        if letter == 'c':
            print(yourname +" you have chosen Wilbur's brick house!\n")

    # A function to ask the player how hard he wants to blow
    try:
        blow_str = int(input("How hard do you want to blow? Choose a value between 0 - 100"))
        if house == 'a' and blow_str >= 20:
                print("You have blown down Rupert's straw house!\n")
                houses_blown += 1
                whose_house.append("a")

        elif house == 'b' and blow_str >= 50:
            print("You have blown down Oscar's wood house!\n")
            houses_blown += 1
            whose_house.append("b")


        elif house == 'c' and blow_str >= 70:
            print("You have blown down Wilbur's brick house!\n")
            houses_blown += 1
            whose_house.append("c")

        else:
            print("Sorry try again!")

    except ValueError:
        print("Invalid input. Please enter a number between 0 -100")

# A function to check how many houses the player has blown down
if houses_blown>= 3:
    print("Congratulations, you have blown down 3 houses! You have won the game")

