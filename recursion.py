# recursion in python
# def sum(n):
#     if (n==1):
#         return 1
#     else:
#         return n+sum(n-1)
# print(sum(10))

# compute CI
# def comp (p,n):
#     if (n==1):
#         return p * (1.1)
#     else:
#         return (comp(p,n-1))*1.1
# print(comp(2000,3))

# factorial
# def fact(n):
#     if (n==1):
#         return 1
#     else:
#         return (fact(n-1))*n
# print(fact(5))

#checking the list has zero 
# def check0 (l):
#     if len(l)==0:
#         return 0
#     if (l[0]==0):
#         return 1
#     else:
#         return check0(l[1:len(l)])
# ans =(check0([1,2,3,4,5]))
# print(ans)

# sorting a list using recursion 

# def mini(l):
#     mini = l[0]
#     for x in l:
#         if (x<mini):
#             mini = x
#     return mini

# def sort(l):
#     # recursively sort the list l
#     if (l==[]) or (len(l)==1):
#         return l
#     #if the list is empty there is nothing to sort
#     m = mini(l)
#     # m contains the minimum most element in l 
#     l.remove(m)
#     # we remove that element from l 
#     return [m]+sort(l)

# l = [5,6,59,15,34,364,61,3,4,1]
# print(sort(l))

'''How can we search for the element k in the given list L '''
 
def obv_search(L,k):
    for x in L:
        if x == k:
            return 1
    return 0

L = list(range(100))
print(L)
print(obv_search(L,300))