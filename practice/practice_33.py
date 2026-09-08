'''
Write a recursive function named triangular 
that accepts a positive integer 
n as argument and returns the sum of the first 
n positive integers.
'''

def triangular(n):
    if n ==  1:
        return 1
    else:
        return n + triangular(n-1)
print(triangular(12))