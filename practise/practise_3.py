# 1. open the text file in 'r' (read) mode
f = open('numbers.txt', 'r')
#2. Initialize the running total.
val = 0
#3. Manually read just the VERY FIRST line of the file to kick things off.
line = f.readline()
#4. A 'While' loop that checks if the string is empty.
# when readline() hits the very end of a file, it returns an empty string('')
while line != "":
    val = val + int(line)
    # if you forget this line, the loop will run forever (an infinite loop)
    line = f.readline()
f.close()
print(val)
