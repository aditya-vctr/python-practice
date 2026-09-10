"""
Write a recursive function named uniq that accepts a non-empty 
list L as argument and returns a new list after removing all duplicates
from it. Your function must retain the last occurrence of each
distinct element in the list.
"""
def uniq(L):
    # 1. THE BASE CASE
    # If the list is 1 item or empty, it's already unique!
    if len(L) <= 1:
        return L
        
    # 2. THE DROP STEP (Duplicate found ahead)
    # If the first item appears again later, we drop it to prioritize the later one.
    if L[0] in L[1:]:
        return uniq(L[1:])
        
    # 3. THE KEEP STEP (Last occurrence)
    # If it doesn't appear again, we keep it and attach it to the rest of the results.
    else:
        return [L[0]] + uniq(L[1:])




    # 1. Standard test with mixed duplicates
print("--- TEST 1: Mixed Duplicates ---")
# Expected: [3, 2, 1, 4] (Keeps the second '2' and second '1')
print("Result:", uniq([1, 2, 3, 2, 1, 4]))

# 2. Test with strings
print("\n--- TEST 2: Strings ---")
# Expected: ['banana', 'apple'] (Keeps the final 'apple')
print("Result:", uniq(['apple', 'banana', 'apple', 'apple']))

# 3. Test with all identical elements
print("\n--- TEST 3: All Identical ---")
# Expected: [5] (Drops all except the very last one)
print("Result:", uniq([5, 5, 5, 5]))

# 4. Test with no duplicates
print("\n--- TEST 4: No Duplicates ---")
# Expected: [10, 20, 30]
print("Result:", uniq([10, 20, 30]))