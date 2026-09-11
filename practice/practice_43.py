"""
Write a recursive function names search that accepts the following arguments:
1.L : a sorted list of integers
2.k : integer
The function should return True if k is found in the list L, and
false otherwise.
"""

def search(L, k):
    if len(L) == 0:
        return False
    mid = len(L) // 2

    if L[mid] == k:
        return True
    elif k < L[mid]:
        return search(L[:mid], k)
    else:
        return search(L[mid+1:], k)

print(search([10,20,30,40,50,60,70,80,90,100], 50)) # true
print(search([10,20,30,40,50,60,70,80,90,100], 69)) # false