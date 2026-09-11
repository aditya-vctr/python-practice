"""
Write a recursive function named uniq that accepts a non-empty
list L as argument and returns a new list after removing all 
duplicates from it. Your function must retain the last 
occurrence of each distinct element in the list.
"""

def uniq(L):
    # 1. if the list is 1 item or empty, it is already unique
    if len(L) <=1:
        return L
    # if the first item appears again later in the list,skip it!
    if L[0] in L[1:]:
        return uniq(L[1:])
    else:
        return [L[0]] + uniq(L[1:])

print(uniq([10,20,10,85,50,80,85]))