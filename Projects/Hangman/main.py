import random
from os import system
from hangmanArt import *
from words import word_list


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
	display.append("_")

while not end_of_game:
	
	guess = input("Guess a letter: ").lower()

	system('cls') #Clean the terminal

	if guess in display:
		print(f"The letter {guess} it've already been guessed")

    #Check guessed letter
	for position in range(word_length):
		letter = chosen_word[position]
		if letter == guess:
			display[position] = letter

    #Check if user is wrong.
	if guess not in chosen_word:
		print(f"The letter {guess} it's not in the word. You lose one life")
		lives -= 1
		if lives == 0:
			end_of_game = True
			print("You lose.\n")

    #Join all the elements in the list and turn it into a String.
	print(f"{' '.join(display)}")

    #Check if user has got all letters.
	if "_" not in display:
		end_of_game = True
		print("You win.")

	print(stages[lives])