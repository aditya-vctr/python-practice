#1. readline(): Reading one line at a time
# it reads exactly one single line from the file.
# it keeps the invisible newline character (\n) at the end of the line

# file = open('names.txt','r')
# line1 = file.readline()
# line2 = file.readline()

# print(repr(line1)) # repr() shows us the raw string with invisible characters
# print(repr(line2))
# file.close()

#2. readlines() : reading everything into a list
# this reads the entire file from top to bottom all at once, and chops it up into a python list.
'''when to use it: when the file is relatively small and you want to quickly store all the lines 
in a list so you can loop through them or access a specific line (eg.) give me the 3rd line'''

# file = open("names.txt", "r")
# all_lines = file.readlines()
# print(all_lines)
# file.close()

#3. line.strip() : The cleanup crew
'it takes messy string and deletes all whitespace (spaces, tabs \t , and newlines \n) from the very beginning and the very end of the text'

# messy_string = "   \n\n  apple  \n  "
# clean_string = messy_string.strip()

# print(repr(messy_string))
# print(repr(clean_string))

# 1. Read all the messy lines into a list
# with open('names.txt', 'r') as file:
#     messy_lines = file.readlines()

# clean_lines =[]
# for line in messy_lines:
#     clean_word = line.strip()
#     clean_lines.append(clean_word)
# print(clean_lines)

# f = open('writing.txt', 'w')
# f.write('One')
# f.write('Two')
# f.write('Three')
# f.write('Four')
# f.write('Five')
# f.close()