'''
Write a recursive function named count that accepts the following 
arguments:
-> L: list of words
-> word: a word, could be any string
This function should return the number of occurrence of word in L
'''


def count(L, word):
    
    # 1. THE BASE CASE
    # If the list is completely empty, the word appears 0 times.
    if len(L) == 0:
        return 0
        
    # 2. THE RECURSIVE STEP - MATCH FOUND
    # Look at the very first item. If it's the word we want:
    if L[0] == word:
        # We count it as 1, and ask the function to check the leftover list
        return 1 + count(L[1:], word)
        
    # 3. THE RECURSIVE STEP - NO MATCH
    # If the first item is a different word:
    else:
        # We count it as 0, and ask the function to check the leftover list
        return 0 + count(L[1:], word)