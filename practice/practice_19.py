
def most_frequent_alpha_character(filename: str) -> str:
    '''
    Arguments:
    filename: str - name of the file

    Return:
    list - the most frequent alphabetic characters (case-sensitive)
    '''
    # extract the text safely using 'with open'
    with open(filename, 'r') as file:
        text = file.read()
    # create a dictionary
    counts = {}

    # filter and count only the alphabetic characters
    for char in text:
        if char.isalpha():
            counts[char] = counts.get(char,0) + 1
    if not counts:
        return []
    # find the absolute highest frequency count
    max_count = max(counts.values())
    winners = []
    for char, count in counts.items():
        if count == max_count:
            winners.append(char)
    return winners
