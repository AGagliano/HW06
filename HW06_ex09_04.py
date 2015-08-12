#!/usr/bin/env python
# HW06_ex09_04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1: he fell off
#       2: elf, eh?
#       3: hello hellhole
##############################################################################
# Imports

# Body
def uses_only(word, s):
	'''Takes a word and a string and returns True if the word contains
	only letters in the list.
	'''
	s_list = []
	for char in s:
		s_list.append(char)
	for letter in word:
		if letter not in s_list:
			return False
	return True

def make_sentence(file_, s):
	
	with open(file_) as f:
		for line in f:
			if uses_only(line.strip(), s) == True:
				print line.strip()


##############################################################################
def main():
      # Call your function(s) here.

    print uses_only('andrea', 'aendr')
    print uses_only('computer', 'phone')

if __name__ == '__main__':
    main()
