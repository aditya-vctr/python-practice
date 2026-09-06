'''
Write a Python function pair_sum_closest(nums, target) that returns the pair of numbers from nums whose sum is closest to target.

Rules:
Return the pair as a sorted tuple.
If multiple pairs are equally close to the target, return the pair with the smaller sum.
If fewer than 2 numbers exist in the list, return None.

Examples:
pair_sum_closest([1, 2, 3, 4], 7) → (3, 4)

pair_sum_closest([1, 5, 10], 8) → (1, 5)

pair_sum_closest([2], 4) → None
'''

def pair_sum_closest(nums, target):

    # If there are fewer than 2 numbers
    if len(nums) < 2:
        return None

    best_pair = None
    best_diff = float("inf")
    best_sum = float("inf")

    # Check every possible pair
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):

            pair_sum = nums[i] + nums[j]
            diff = abs(pair_sum - target)

            # Check if this pair is better
            if diff < best_diff or (diff == best_diff and pair_sum < best_sum):
                best_diff = diff
                best_sum = pair_sum
                best_pair = tuple(sorted((nums[i], nums[j])))

    return best_pair

print(pair_sum_closest([1, 2, 3, 4], 7)) #(3,4)
print(pair_sum_closest([1, 5, 10], 8))   #(1,5)
print(pair_sum_closest([2], 4))          # None
