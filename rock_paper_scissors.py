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
print("Enter your choice in word (rock/paper/scissors)!")

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

# Result printing
def printMsg(user_winner,draw):
	print("...\nResult:")
	if draw:
		print("Draw!")
	else:
		if user_winner:
			print("Congratulation! You won.")
		else:
			print("You lost. Better luck next time!")

def gamePlay(user_choice,com_choice):
	if user_choice == com_choice:
		draw = True
		user_winner = False
	else:
		draw = False
		if user_choice == "ROCK":
			if com_choice == "PAPER":
				user_winner = False
			if com_choice == "SCISSORS":
				user_winner = True
		elif user_choice == "PAPER":
			if com_choice == "ROCK":
				user_winner = True
			if com_choice == "SCISSORS":
				user_winner = False
		elif user_choice == "SCISSORS":
			if com_choice == "PAPER":
				user_winner = True
			if com_choice == "ROCK":
				user_winner = False
	printMsg(user_winner,draw)

gamePlay(user_choice,com_choice)




