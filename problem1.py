'''write a function reverse_each_word(words) that takes a  list of strings as input and returns a new  list where each word is reversed .
Assumes that all elements in the list are strings.
reverse_each_word(["apple", "cat", "python"] -> ["elppa", "tac", "nohtyp"]
teach me'''
def reverse_each_word(words):
    reversed_list = []
    for word in words:
        # FIX 1 & 2: Added 'word' and used [::-1] to reverse it
        reversed_word = word[::-1]
        
        # FIX 3: Indented this line so it runs for EVERY word inside the loop
        reversed_list.append(reversed_word)
        
    return reversed_list

print(reverse_each_word(["sawant", "sinu"]))


    