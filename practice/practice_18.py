
def valid_substring(s: str, word_list: list) -> bool:
    '''
    Arguments:
    s: str - the string to be checked
    word_list: list - a list of valid words

    Return:
    bool - True if the string can be split into two valid words, False otherwise
    '''
    valid_words = set(word_list)
    for i in range(1,len(s)):
        left_part = s[:i]
        right_part =s[i:]
        if left_part in valid_words and right_part in valid_words:
            return True
    return False

print(valid_substring('applebanana', ['apple', 'banana', 'pine', 'melon']))
