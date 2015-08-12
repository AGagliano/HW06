#!/usr/bin/env python
# HW06_ex09_03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write function(s)
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

from itertools import combinations

# Body

## Code for #1
# def avoids(word, s):
# 	'''Takes a word and a string of forbidden characters (s) as inputs, 
# 	and returns True if the word doesn't use any of the forbidden characters.
# 	'''
# 	forbidden_list = []

# 	for char in s:
# 		forbidden_list.append(char)
	
# 	for i in forbidden_list:
# 		if i in word:
# 			return False
# 	return True

def tests_word(word, s):
	'''Takes a word and a string of forbidden characters (s) as inputs, 
	and returns True if the word doesn't use any of the forbidden characters.
 	'''
	#Create a list to hold the forbidden characters.
	forbidden_list = []

	#Partitions characters in the forbidden string into the list.
	for char in s:
		forbidden_list.append(char)
	
	#Tests if each forbidden character exits in the given word.
	for i in forbidden_list:
		if i in word:
			return False			#Returns False upon first instance of a forbidden char
	return True						

def counts_words(file_, s):
	'''Counts the number of words in a given text file that don't contain
	the given forbidden letters.
	'''
	count = 0
	
	with open(file_) as f:
		for line in f:
			if tests_word(line.strip(), s) == True:
				count += 1
	#print "{0} words of {1} don't contain those forbidden letters.".format(count, file_)
	return count

def find_optimal_combo(file_):
	'''Finds a combination of 5 forbidden letters that excludes the smallest
	number of words from the given text file. Function prints the 5-letter combination
	and prints the number of words excluded. 
	'''
	
	#Create a list of the alphabet using ASCII code
	alphabet = []
	for i in range(97,123):
		alphabet.append(chr(i))
	print alphabet

	#Find the total number of words in the text file
	with open(file_) as f:
		total_words = sum(1 for line in f)
	
	#Find all the combinations of 5 forbidden letters.
	#Then counts words in text file that don't contain those letters.
	#Note, the 5 forbidden letters are all unique. 
	#For example, 'aabcd' is not assumed to be a forbidden string.
	words_excluded = total_words
	combo = None
	for subset in combinations(alphabet, 5):					
		words_included = counts_words(file_, str(subset))
		if (total_words - words_included) < words_excluded:
			words_excluded = total_words - words_included
			combo = str(subset)
	print "The optimal 5-letter combination of forbidden letters is {0}".format(combo)
	print "Number of words excluded: {0}".format(words_excluded)




##############################################################################

	# #Code to make string combinations without itertools.
	# #But, the program times out. 
	# 
	# s = None
	# for i in range(0, 25):
	# 	p = alphabet[i]
	# 	for j in range(1, 25):
	# 		q = p + alphabet[j]
	# 		for k in range(2, 25):
	# 			r =  q + alphabet[k]
	# 			for l in range(3, 25):
	# 				t = r + alphabet[l]
	# 				for m in range(4, 25):
	# 					u = t + alphabet[m]
	# 					return u

##############################################################################

	## Code to make string combinations without itertools, using recursive function.
	## But, variable x needs to be different at each iteration (couldn't figure out).
	# def create_combos(s, r, count = 0):
	# 	#s is string, in this case alphabet
	# 	#r is combination size
	# 	#count is used so that the function can recursively call itself
	# 	print type(s)
	# 	s_length = len(s)

	# 	for i in range(count, s_length - 1):
	# 		x = s[i]
	# 		count += 1
	# 		create_combos(count, s)
	# 	print x


##############################################################################
def main():
   
	## Tests for #1
    # print avoids('WATER', 'bottle')		#True
    # print avoids('peanut', 'butter')		#False
    # print avoids('not excited', '!')		#True
    # print avoids('SHOOTING', 'happy')		#True
    # print avoids('oneword', ' ')			#True

    ## Tests for #2
    #forbidden = raw_input('Enter forbidden letters\n>')
    #counts_words('words.txt', forbidden)

	## Test for #3 (don't run because times out)
	#find_optimal_combo('words.txt')


if __name__ == '__main__':
    main()
