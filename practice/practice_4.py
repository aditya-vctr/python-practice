'''
Name,Gender,Age
Sam,M,20
Samyuktha,F,25
Samit,M,30
Sampoorna,F,35
Write a program that extracts the last column from the file and prints it to the console. 
Ignore the header. There shouldn't be any extra lines between consecutive lines in the output.'''

f = open('student.csv','r')
#1. skip the header line by reading it and doing nothing with it
f.readline()
#2. loop through remaining lines in the file 
for line in f:
    #3. clen the invisible \n and split the text by commas
    row_data = line.strip().split(',')
    print(row_data[-1])
f.close()