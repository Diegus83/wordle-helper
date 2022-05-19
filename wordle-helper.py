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

	letters = input("Enter gray square letters, press Enter when done: ")

	for letter in letters:
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
	global word_list
	good_ones = list()

	letters = input("Enter yellow square letters, press Enter when done: ")

	for letter in letters:
		for index, word in enumerate(word_list):
			if word and letter not in word:
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
	known_letters = {1:'', 2:'', 3:'', 4:'', 5:''}
	good_ones = list()
	
	print("Enter a letter for positions 1-5 or press Enter to skip")
	for key in known_letters.keys():
		known_letters[key] = input(f'Position {key}: ')
	
	for key, letter in known_letters.items():
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

		else:
			print(f'Invalid option, please choose a number between {menuKeys[0]} and {menuKeys[-1]}')

