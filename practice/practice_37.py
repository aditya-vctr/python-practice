'''
Given a text file log.txt where each line contains a log message, write a function count_errors()
that reads the file and returns the number of lines containing the word "ERROR"
Matching is case-sensitive, meaning only the exact uppercase word "ERROR" should be counted.
Example file: log.txt
info server started
ERROR Database Failed
Warning Low Memory
ERROR Timeout Occurred

Expected output
input: log.txt
output: 2
'''

def count_errors():
    count = 0
    with open('log.txt', "r") as file:
        for line in file:
            if 'ERROR' in line:
                count += 1
    return count
print(count_errors())