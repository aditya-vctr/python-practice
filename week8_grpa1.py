'''filename is a text file that contains a collection of words in lower case, one word on each line. 
Write a function named get_freq that accepts filename as argument. 
It should return a dictionary where the keys are distinct words in the file, 
the values are the frequencies of these words in the file.
For example, given the following file:
good
great
good
work
work '''
# so our job is:
# 1. open the file.
# 2. Read each line.
# 3. Remove the newline.
# 4. Put the word into a dictionary.
# 5. if the word already exists- increase the count.
# 6. otherwise- start its count at 1.
# 7. Return the dictionary.

def get_freq(filename):
    result = {}
    with open(filename,"r") as file:
        for line in file:
            word = line.strip()
            if word in result:
                result[word]+=1
            else:
                result[word] = 1
    return result

