'''
Write a recursive function named multiply accepts two positive
integers 
a and b as argument and returns their product. You can only 
use + and - operators. You are not allowed to use the 
* symbol anywhere in your code!
'''

def multiply(a,b):
    if b == 1:
        return a 
    else:
        return a + multiply(a, b-1)

print(multiply(4,3))