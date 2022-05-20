#!/usr/bin/env python3

import os
import pprint
import time

def printWords(flag):
	if not flag:
		global word_list
		pprint.pprint(word_list, compact = True)
		print('')
	else:
		print(f'The current list contains {len(word_list)} words')

def printMenu():
	global menuOptions
	for key in menuOptions.keys():
		print(f'{key} - {menuOptions[key]}')

def quitConfirmation():
	a = input("You want to exit? y/n: ")

	if a == 'y':
		print("Ok byeee!")
		exit()
	else:
		print("Keeping current list")

def getLetters(color):
	"Ask the user for five letters and saves them in order"

	letters = {1:'', 2:'', 3:'', 4:'', 5:''}
	
	# print(f'''
	# 	{letters[1]}\t{letters[2]}\t{letters[3]}\t{letters[4]}\t{letters[5]}
	# 	-\t-\t-\t-\t-
	# 	1\t2\t3\t4\t5
	# 	''')

	print(f'Enter the letters for the {color} squares 1-5, press Enter to skip')
	for key in letters.keys():
		letters[key] = input(f'Position {key}: ')

	return letters
	
def resetConfirmation():
	global word_list

	a = input("You want to reload the full list of words? y/n: ")

	if a == 'y':
		word_list = loadWordList()
	else:
		print("Keeping current list")

def waitAnimation():
	chars = ["––", "\\", "|", "/"]
	for i in range(4):
		for c in chars:
			os.system("clear")
			print(f'Filtering out words, please wait...{c}')
			time.sleep(0.1)

def loadWordList() -> list:
	"Loads the list of all five letter words"
	words = list()
	with open('wordle-words.txt', 'r') as fin:
		for word in fin:
			words.append(word[0:5])
	return words

def graySquares():
	"Filter words using a bad letter (gray squares)"
	global word_list
	good_ones = list()
	letters = getLetters('gray')

	for key, letter in letters.items():
		if letter:
			for index, word in enumerate(word_list):
				if word and letter in word:
					word_list[index] = False

	for word in word_list:
		if word:
			good_ones.append(word)

	word_list = good_ones

	waitAnimation()
	return None

def yellowSquares():
	"Filter words missing a known letter (yellow squares)"
	# this function needs to do double filtering:
	# eg. a yellow S on the first square means:
	# remove all the words that don't have an S
	# but also remove all the words that have an S in the first square

	global word_list
	good_ones = list()
	letters = getLetters('yellow')
	
	for key, letter in letters.items():
		if letter:
			for index, word in enumerate(word_list):
				# if word[key] is the yellow letter I can discard that word
				if word and word[key-1] == letter:
					word_list[index] = False
				# if word doesn't contain the yellow letter in another position
				# I can discard that word too
				elif word and letter not in word:
					word_list[index] = False

	for word in word_list:
		if word:
			good_ones.append(word)

	word_list = good_ones

	waitAnimation()
	return None

def greenSquares():
	"Filter words missing a known letter and position (green squares)"
	global word_list
	good_ones = list()
	letters = getLetters('green')
	
	for key, letter in letters.items():
		if letter:
			for index, word in enumerate(word_list):
				if word and word[key-1] != letter:
					word_list[index] = False

	for word in word_list:
		if word:
			good_ones.append(word)

	word_list = good_ones

	waitAnimation()
	return None

menuOptions = {
	1: "Print current list of words",
	2: "Filter words using a bad letter (gray squares)",
	3: "Filter words missing a known letter (yellow squares)",
	4: "Filter words missing a known letter and position (green squares)",
	5: "Start over",
	6: "Quit"
}

menuKeys = [x for x in menuOptions.keys()]

if __name__ == "__main__":
	
	os.system("clear")

	word_list = loadWordList()

	while True:
		printWords(True)
		printMenu()
		
		try:
			option = int(input("Select: "))
		except:
			option = 9999

		if option == 1:
			printWords(False)
		elif option == 2:
			graySquares()
		elif option== 3:
			yellowSquares()
		elif option == 4:
			greenSquares()
		elif option == 5:
			resetConfirmation()
		elif option == 6:
			quitConfirmation()
		elif option == 66:
			exit()

		else:
			print(f'Invalid option, please choose a number between {menuKeys[0]} and {menuKeys[-1]}')

