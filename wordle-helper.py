#!/usr/bin/env python3

def loadWordList() -> list:
	"Loads the list of all five letter words"
	words = list()
	with open('wordle-words.txt', 'r') as fin:
		for word in fin:
			words.append(word[0:5])
	return words


def graySquares(letters: list):
	"Filter words using a bad letter (gray squares)"
	return None

def yellowSquares(letter: str, position: int):
	"Filter words missing a known letter (yellow squares)"
	return None

def greenSquares(letters: list):
	"Filter words missing a known letter and position (green squares)"
	return None

def printWords(flag):
	if not flag:
		global word_list
		for word in word_list:
			print(word, end='\t')
		print('')
	else:
		print(f'The current list contains {len(word_list)} words')

def printMenu():
	global menuOptions
	for key in menuOptions.keys():
		print(f'{key} - {menuOptions[key]}')

def quitConfirmation():
	print("Ok byeee!")
	exit()


word_list = loadWordList()

menuOptions = {
	1: "Print current list of words",
	2: "Filter words using a bad letter (gray squares)",
	3: "Filter words missing a known letter (yellow squares)",
	4: "Filter words missing a known letter and position (green squares)",
	5: "Quit",
	6: "Start over"
}

menuKeys = [x for x in menuOptions.keys()]

if __name__ == "__main__":
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
			quitConfirmation()
		elif option == 6:
			loadWordList()

		else:
			print(f'Invalid option, please choose a number between {menuKeys[0]} and {menuKeys[-1]}')

