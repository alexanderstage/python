def break_words(stuff):
	"""This function will break up words for us."""
	# Spit method breaks the string into a list using whitespace
	# as a delimiter 
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sort the words"""
	# sorted method sorts the words in the list alphabetically
	return sorted(words)

def print_first_word(words):
	"""prints the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes ina full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)


# These 2 use the above functions directly to transform the data

def print_first_and_last(sentence):
	"""Prints the first and last words of a sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
 
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)