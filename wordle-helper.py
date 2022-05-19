#!/usr/bin/env python3

def loadWordList() -> list:
	"Loads the list of all five letter words"
	words = list()
	with open('wordle-words.txt', 'r') as fin:
		for word in fin:
			words.append(word[0:5])
	return words


def filterBadLetters(letters: list):
	"Eliminates words based on bad letter guesses"

	return None

def filterKnownPositions(letter: str, position: int):
	"Eliminates words based on known letters and positions"

	return None

def filterGoodLetters(letters: list):
	"Eliminates words that don't contain a known good letter"

	return None

def printWords():
	global word_list
	print(word_list)

word_list = loadWordList()

while True:
	print(f'The current list contains {len(word_list)} possible words')
	print('- Choose an option to elimitate words from the list')
	print('- Eliminate words that contain a bad letter (1)')
	print('- Elminate words that are missing a good letter (2)')
	print('- Eliminate words that don\'t have a letter in a known position (3)')
	print('- Print list (p)')
	print('- Quit (q)')
	selection = input("Choose an option: ")
	if selection == 'q':
		print('Ok, bye!' )
		break
	elif selection == 'p':
		printWords()