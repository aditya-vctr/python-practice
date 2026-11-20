def common_chars(word1: str, word2: str) -> str:
    '''
    Find all unique common characters present in both word1 and word2
    and return them as a string sorted in ascending order.
    Example:
    >>> common_chars('apple', 'ball')
    'al'
    '''

    result = set()

    for i in range(len(word1)):
        if word1[i] in word2:
            result.add(word1[i])
    return "".join(sorted(result))

print(common_chars('apple', 'ball'))