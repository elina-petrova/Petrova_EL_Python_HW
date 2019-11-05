#import the random package so that we can generate a random choice 
from random import randint
from gameFunctions import winloss
from gameFunctions import comparison


#set up some variables for player and AI lives
player_lives = 5
computer_lives = 5

# choices is an array => an array is a container that can hold multiple valves.
choices= ["rock", "paper", "scissors"]

# set the computer variable  to one  of these choices
computer = choices[randint(0, 2)]

#set up the game loop so that we dont have to restart all the time 

player = False 


while player == False:
	print("*******************************\n\n")
	print("Computer lives: ", computer_lives, "/5\n")
	print("Player lives: ", player_lives, "/5\n")
	print("Choose your weapon!\n\n")
	print("*****************\n\n")

	player = input("choose rock, paper ot scissors: ")
	print("*****************")

	print("computer chose ", computer, "\n")
	print("player chose ", player, "\n")

	comparison.compare(player, computer, computer_lives, player_lives)
	



	#handle all lives lost for player or AI
	if player_lives is 0:
		winloss.winorlose("lost")
		#print("You are out of lives! You suck at this game. Would you like to play again?")
		#choice = input("Y / N")
		#print(choice)

		#if (choice is "N") or (choice is "n"):
			#print("You chose to quit.")
			#exit()
		#elif (choice is "Y") or (choice is "y"):
			#reset the game so that we can start all over again
			#player_lives = 5
			#computer_lives = 5
			#player = False
			#computer = choice[randint(0,2)]

	elif computer_lives is 0:
		winloss.winorlose("won")
        	# 	print("Computer is out of lives! You rock at this game. Would you like to play again?")
	# 	choice = input("Y / N")
	# 	print(choice)

	# 	if (choice is "N") or (choice is "n"):
	# 		print("You chose to quit.")
	# 		exit()
	# 	elif (choice is "Y") or (choice is "y"):
	# 		#reset the game so that we can start all over again
	# 		player_lives = 5
	# 		computer_lives = 5
	# 		player = False
	# 		computer = choice[randint(0,2)]

  
    	#need ro check all of our comditions after checking for a tie
	player = False;
	computer = choices[randint(0, 2)]
