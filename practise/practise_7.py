# Your Task:
# Write a function named get_high_scores(filename) that accepts the filename as an argument
# The function should return a dictionary where the keys are the player names (strings) and the values are their scores (integers).

def get_high_scores(filename):
    f = open(filename,'r')
    f.readline()
    score_dict = dict()
    for line in f:
        parts = line.strip().split(',')
        player =parts[0]
        score_string = parts[1]
        score_dict[player] = int(score_string)
    f.close()
    return score_dict

# Write a function named get_matrix that accepts the filename as argument.
# It should return the matrix as a list of lists. Each cell of the matrix should be an integer and not a string.
def get_matrix(filename):
    matrix =[]
    f = open(filename,'r')
    for line in f:
        string_parts  = line.strip().split()

        current_row = []
        for item in string_parts:
            num = int(item)
            current_row.append(num)
        
        matrix.append(current_row)
    f.close()
    return matrix

# Write a function named get_score_grid(filename) that accepts the filename as an argument.
# The function should return the data as a list of lists, where every single score is converted into an integer.

# Expected Output:
# [[85, 90, 92], [78, 81, 80], [95, 99, 98]]


def get_score(filename):
    grid =[]
    f = open(filename,'r')
    for line in f:
        string_parts = line.strip().split(',')

        student_scores  = []
        for item in string_parts:
            score = int(item)
            student_scores.append(score)
        grid.append(student_scores)
    f.close()
    return grid