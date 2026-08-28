# Python file detection 

#Excercise 1 - Read a file
# file = open("hello.txt", "r")
# content = file.read()  # reading a file 
# print(content)
# file.close() # closing a file


#Excercise 2 - Store the content
''' Create students.txt:
Aditya
Rahul
Priya
Neha
Write code that reads the entire file and stores it in a variable called content.
Then print:
print(content) '''

# file = open("student.txt","r")
# content = file.read()
# print(content)
# file.close()

# file = open("hello.txt", "r")
# print(file.read())
# file.close()

# with open("hello.txt", "r") as file:
#     print(file.read())

# file = open("names.txt", "r")
# for line in file:
#     print(line.strip())
# file.close()

# file = open("test.txt", "w")
# file.write("I am learning Python")
# file.close()

file = open("student.txt", "a")
file.write("\ncharlie")
file.close()