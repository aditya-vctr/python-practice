# 1. opens the file 'words.txt' in 'r' (read) mode so we can look at its contents.
f = open('words.txt', 'r')

# 2. starts a loop that grabs one line of text from the file at a time.
for line in f:
    # 3. line[-1] looks at the very last character of the current string.
    if line[-1] == "\n":

        # 4. If it is a newline, print this statement.
        print('Last character of this line is a newline')

    # 5. If the last character is NOT '\n' (meaning it is a normal letter like "e")
    else:

        #6. print this alternative statement.
        print('Last character of this line is not a newline')
#7. closes the file to free up computer memory (best practise!)
f.close()