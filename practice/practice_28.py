# Count Odd 3 Digit Numbers (Ignore None)

def count_odd_three_digit_nums(nums):
    count = 0
    for num in nums:
        if num is not None:
            if 100 <= abs(num) <= 999 and num % 2 == 1:
                count += 1
    return count

print(count_odd_three_digit_nums([101, -203, None, 99, 300]))
print(count_odd_three_digit_nums([10, 305, 507, 99]))