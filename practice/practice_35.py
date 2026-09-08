'''
Consider a positive integer x that is a power of 2. The logarithm of x
to the base 2 is the number of times 2 has to be multiplied with itself
so get x, and is denoted by log2(x). for example, log2(4) = 2.
Note that log2(1) = 0.
'''

def logarithm(x):
    if x == 1:
        return 0
    else:
        return 1 + logarithm(x//2)

print(logarithm(4))
