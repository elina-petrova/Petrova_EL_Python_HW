#import the random package so that we can generate a random choice 
from random import randint




# choices is an array => an array is a container that can hold multiple valves.
choices= ["rock", "paper", "scissors"]

# set the computer variable  to one  of these choices
computer = choices[randint(0, 2)]

#set up the game loop so that we dont have to restart all the time 

player = False 
while player == False:
	print("*******************************\n\n")
	print("Choose your weapon!\n\n")
	print("*****************\n\n")

	player = input("choose rock, paper ot scissors: ")
	print("*****************")

	print("computer chose ", computer, "\n")
	print("player chose ", player, "\n")

	if player.lower() =="quit":
		exit()
	elif computer == player.lower():
		print("tie! no one wins, play again")

	elif player.lower() == "rock":
		if computer == "paper":
			print("Y O U    L O S E ! ", computer, "covers", player, "\n")
		else:
			print("Y O U  W I N ! ", player, "smashes", computer, "\n")

	elif player.lower() == "paper":
		if computer == "scissors":
			print("Y O U    L O S E ! ", computer, "cuts", player, "\n")
		else:
			print("Y O U  W I N ! ", player, "smashes", computer, "\n")

	elif player.lower() == "scissors":
		if computer == "rock":
			print("Y O U    L O S E ! ", computer, "smashes", player, "\n")
		else:
			print("Y O U  W I N ! ", player, "cuts", computer, "\n")

	else:
		print("That's not a valid choice, try again")



	#need ro check all of our comditions after checking for a tie
	player = False;
	computer = choices[randint(0, 2)]
