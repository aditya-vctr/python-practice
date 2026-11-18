def is_odd_indices_alpha_and_even_indices_digits(string: str) -> bool:
    '''
    Return True if all characters at even 0-based indices (0, 2, 4, ...) are digits
    AND all characters at odd 0-based indices (1, 3, 5, ...) are alphabets;
    return False otherwise.
    Examples:
    >>> is_odd_indices_alpha_and_even_indices_digits("1a2b3c")
    True
    >>> is_odd_indices_alpha_and_even_indices_digits("a1b2")
    False
    '''
    for i in range(len(string)):
        if i % 2 == 0 and not string[i].isdigit():
            return False
        if i % 2 == 1 and not string[i].isalpha():
            return False

    return True
print(is_odd_indices_alpha_and_even_indices_digits("1a2b3c"))