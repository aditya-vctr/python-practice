''' write a function named read_line that accepts a text file named
positive integer n as arguments. within the function, read the file
and return the nth line of the file. if the file has fewer than n lines,
return the string 'None'.'''
# def read_line(filename,n):
#     f = open(filename,'r')
#     for i in range(n):
#         line = f.readline()
#         if line == "":
#             f.close()
#             return 'None'
#     f.close()
#     return  line

'''Write a function named get_max_line that accepts
 a text file named filename as argument. 
Each line in this file contains an integer. The function should
 return the line number that houses the maximum integer in the 
 file. If multiple lines have the same maximum number, 
 return the smaller of the two. Line numbers start from one and 
 not zero.'''

def get_max_line(filename):
    f = open(filename,'n')
    max_val = None
    max_line_num = 0
    current_line = 1
    for line in f:
        num = int(line)
        if max_val is None or num > max_val:
            max_val = num
            max_line_num = current_line
        current_line = current_line + 1

    f.close()

    return max_line_num