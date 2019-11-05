	


def compare(player, computer, computer_lives, player_lives):


	if player.lower() =="quit":
		exit()
	elif computer == player.lower():
		print("tie! no one wins, play again")

	elif player.lower() == "rock":
		if computer == "paper":
			print("Y O U    L O S E ! ", computer, "covers", player, "\n")
			player_lives = player_lives - 1
		else:
			print("Y O U  W I N ! ", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower() == "paper":
		if computer == "scissors":
			print("Y O U    L O S E ! ", computer, "cuts", player, "\n")
			player_lives = player_lives - 1
		else:
			print("Y O U  W I N ! ", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower() == "scissors":
		if computer == "rock":
			print("Y O U    L O S E ! ", computer, "smashes", player, "\n")
			player_lives = player_lives - 1
		else:
			print("Y O U  W I N ! ", player, "cuts", computer, "\n")
			computer_lives = computer_lives - 1

	else:
		print("That's not a valid choice, try again")

	return player, computer, computer_lives, player_lives