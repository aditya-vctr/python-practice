'''
Write a Python function deinterleave(s: str) -> str that takes a string s as input and returns a new string where:
Characters at even indices are placed first.
Characters at odd indices are placed after them.
'''
'''
Examples:
deinterleave("abcdef") → "acebdf"
deinterleave("12345") → "13524"
'''

def deinterleave(s: str) -> str:
    result = ""

    # Add characters at even indices
    for i in range(0, len(s), 2):
        result += s[i]

    # Add characters at odd indices
    for i in range(1, len(s), 2):
        result += s[i]

    return result

print(deinterleave("abcdef")) #  acebdf
print(deinterleave("12345"))  #  13524