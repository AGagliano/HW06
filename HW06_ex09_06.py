#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write function(s) to assist you
#   - number of abecedarian words:
##############################################################################
# Imports

# Body

def is_abecedarian(word):
	'''Returns True if the letters in a given word appear in alphabetical
	order (double letters are okay).
	'''
	for i in range(0,len(word)-1):
		if ord(word[i]) > ord(word[i+1]):
			return False
	return True

def num_abecedarian(file_):
	'''Takes a file of words and returns the number of abecedarian words.
	'''
	count = 0
	with open(file_) as f:
		for line in f:
			if is_abecedarian(line.strip()) == True:
				count +=1
		print count


##############################################################################
def main():
    print is_abecedarian('aabbcc')			#True
    print is_abecedarian('chocolate') 		#False
    num_abecedarian('words.txt')

if __name__ == '__main__':
    main()
