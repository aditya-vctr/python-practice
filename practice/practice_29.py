'''
Write a program that takes a list of full names and outputs their initials 
(except the last name) followed by the full last name. The output should be 
sorted alphabetically.

An initial is the first letter of each part of a name.

Assume that the names are given in the correct case.

Hint: Use sorted function or list.sort to sort the list

Input Format

First line contains the number of names, n.
Next n lines contain one full name per line.
Output Format

Output the processed names in sorted order, one per line.
Example
Input:
3
John Doe
Alice Johnson
Bob Alan Rickman

Output:
A. Johnson
B. A. Rickman
J. Doe
'''

# defining a function
def format_name(full_name: str) -> str:
    parts = full_name.split()
    last_name = parts[-1]
    other_parts = parts[:-1]

    initials = []
    for name in other_parts:
        initials.append(name[0] + ".")

    final_pieces = initials + [last_name]
    return " ".join(final_pieces)

# Main code that function uses
n = int(input())
formatted_names = []
for i in range(n):
    # read the raw name
    raw_name = input().strip()

    abbriviated_name = format_name(raw_name)
    formatted_names.append(abbriviated_name)

#sort and print
formatted_names.sort()

for name in formatted_names:
    print(name)