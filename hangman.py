# import random

# # A list of words that 
# potential_words = ["anime", "meme", "knukles", "wkanda", "pizza"]

# word = random.choice(potential_words)


# Use to test your code:
# print(word)

# Converts the word to lowercase
# word = word.lower()

# Make it a list of letters for someone to guess
 # TIP: the number of letters should match the word

# print(guess in secret_word)
    # if guess in secret_word:
	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!







secret_word = "pizza"
sw_len = len(secret_word)
# secret_word = ["p"", "i", "z", "z", "a"]

# Some useful variables
guesses = ["_", "_","_","_", "_"]
userguess = "0"
print(guesses)
if(userguess in secret_word):
	for "p" in range(0, 5)
		if(secret_word["p"] == userguess):
			guesses[i] = userguess
maxfails = 15
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")
  for"p" in range(0,5):
    if secret_word["p"] == userguess :
fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")