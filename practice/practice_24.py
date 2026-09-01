# Check if a String Starts and Ends with the Same Vowel

def starts_and_ends_with_same_vowel(s: str) -> bool:
    '''
    Given a string, check if it starts and ends with the same vowel (case insensitive).

    Eg.
    starts_and_ends_with_same_vowel("Apple") -> False
    starts_and_ends_with_same_vowel("Atta") -> True
    starts_and_ends_with_same_vowel("Tart") -> False
    starts_and_ends_with_same_vowel("umbrella") -> False

    Args:
        s (str): Input string.

    Returns:
        bool: True if the string starts and ends with the same vowel, else False.
    '''
    if not s:
        return False
    first_letter = s[0].lower()
    last_letter = s[-1].lower()

    vowels = 'aeiou'
    if first_letter in vowels and first_letter == last_letter:
        return True
    else:
        return False

print(starts_and_ends_with_same_vowel("Elephant")) #False
print(starts_and_ends_with_same_vowel("Apple"))    #False
print(starts_and_ends_with_same_vowel("Atta"))     #True