'''As a convention, while writing to a file, the last line will not have a '\n' at the end. Accept a positive integer 
n as input and write the first n positive integers to a file named numbers.txt, one number on each line.'''

# 1. Ask the user for a positive integer and convert  it from a string to an integer.
n = int(input())
#2. open (or create) the file 'numbers.txt' in 'w' write mode.
f = open('numbers.txt', 'w')
for x in range(1,n+1):
    # f.write() only excepts strings so we must convert the number into text.
    line = str(n)
    #  CRUCIAL RULE: check if this is the last number.
    # if x is not equals to n (meaning it's not the last number yet)...
    if x != n:
        # add the  invisible newline character to push the next number down 
        line = line + "\n"
        # write the final formatted string to the file
    f.write(line)
f.close()