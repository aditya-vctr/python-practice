'''
Write a recursive function named palindrome that accepts a
string word as argument and returns True if it is a palindrome
and False otherwise.
'''

def palindrome(word):
    if len(word) <= 1:
        return True
    # The recursive step
    # if the outer letters match, chop them off and check inside
    if word[0] == word[-1]:
        return palindrome(word[1:-1])
    else:
        return False

print(palindrome("malayalam"))
