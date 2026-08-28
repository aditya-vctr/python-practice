'''print hollow x pattern 
given an integer n(where  n>=3) print a hollow x-shaped pattern using * 
the pattern should contain:
A * on the main diagonal 
A * on the secondary diagonal.
spaces between the * character where appropriate if both  diagonals meet at the same position, print only one *
Note- do not print trailing spaces at the end of any line.'''
def print_hollow_x(n):
    # Loop through every row (i)
    for i in range(n):
        
        # Calculate where the row should end to avoid trailing spaces
        last_star = max(i, n - 1 - i)
        
        # We will build the row character by character
        row_str = ""
        
        # Loop through the columns (j), but ONLY up to the last star
        for j in range(last_star + 1):
            
            # Apply our two mathematical rules!
            if j == i or (i + j) == n - 1:
                row_str += "*"
            else:
                row_str += " "
                
        # Print the fully built row
        print(row_str)

# Test it
n = int(input())
print_hollow_x(n)