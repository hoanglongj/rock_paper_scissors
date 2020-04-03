## ROCK, PAPER, SCISSORS GAME
## A hand game played between the user and the computer
## Each player performs one of three shapes with an outstretched hand
## Scissors beats Paper
## Paper beats Rock
## Rock beats Scissors

# Import modules
from random import randint

# Welcome message
print("Welcome to ROCK PAPER SCISSORS GAME!\n")
print("Enter your choice in word (rock/paper/scissors)")

# Possible options
options = ["ROCK","PAPER","SCISSORS"]

# Getting user choice
user_choice = input("What is your choice? ")
user_choice = user_choice.upper();

# Getting computer choice
index = randint(0,2)
com_choice = options[index]

# Printing input choice
print("...")
print("Your choice: %s" % user_choice)
print("Computer choice: %s" % com_choice)





