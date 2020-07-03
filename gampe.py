"""
	this game helps users to guess a number
	Plan:
		Show instruction to user
		Set score to zero
		While user is still wiling to play:
			get a corretn guess
			increment the score
"""

import random

def showUserInstruction():
	"""This function show instruction to user """
	message = "Ok {} Now's time to play. Are you ready? "
	print("Hello, Gammie!")
	username = input('Please, how do you want to be addressed? ')
	print('Thanks!')
	print (message.format(username))



def getCorrectGuess(chances):
	# get a randomn integer
	correctGuess = random.randint(1, 50)

	# get an input from the user
	guess = input('Enter a guess: ')
	# convert guess to integer
	guess = int(guess)
	chances = chances - 1
	while guess != correctGuess:
		while chances > 0:
			message = 'Oooops!'
			if guess > correctGuess:
				message += '\tYour guess is higher.'
			elif guess < correctGuess:
				message += '\tYour guess is lower.'
			message += '\tPlease enter another guess: '
			guess = input(message)
			# convert guess to integer
			guess = int(guess)

			# update the chances
			chances = chances - 1
		print('Game over.')
		return None
	# we found the corret guess
	print(f'Wao! You have a good guess of {guess}. How cool is that? ')
	return True



def runGame():
	# set score to zero
	score = 0
	# get the number of guess
	chances = int(input("How many times do you weant to make a guess? "))
	print(f'You will be able to make a guess {chances} times.')
	exit = 'exit'
	exitCommand = ''
	while exit != exitCommand:
		# get a corretn guess
		if getCorrectGuess(chances) == True:
			# update user score
			score += 5

		# show user score
		print(f'\n\n\t\tYour score is {score}.\n')

		# check if the user wants to play again?
		exitCommand = input("Want to run again? type 'exit' to quit: ")
		exitCommand = exitCommand.strip()

	# show user his/her score
	print(f'\nWao , You made it to this point. \n\n\t\tYour score is {score}.\n')

def main():
	""" This function is the starting point for our game application"""
	
	# Show instruction to user
	showUserInstruction()

	# run the game
	runGame()
			




if __name__ == '__main__':
	main()
