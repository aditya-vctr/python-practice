'''
Given the number of lines n and a text with n lines, print the frequency of each word in lowercase.
words should be compared case-insensitively. convert every word to lowercase before counting. 
Print each distinct word along with its frequency, one per line, in the order of its first appearance.

Input format:
-> The first line contains an integer n, the number of lines.
-> The next n lines  contain the input text.

Output format:
Print each distinct word and its frequency, separated by a space, one per line, in the order in which 
each word first appears.

Example:
input:
2
Hello hello
World HELLO

output:
hello 3
world 1
'''
n = int(input("enter a num of line: "))

frequency = {}
order = []
for _ in range(n):
    line = input()
    for word in line.split():
        word = word.lower()

        if word not in frequency:
            frequency[word] = 1
            order.append(word)
        else:
            frequency[word] += 1
for word  in order:
    print(word, frequency[word])