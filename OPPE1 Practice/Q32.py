def get_roll_nos(data: list, criteria=None):
    '''
    Given data as a list of (rollno, marks) tuples and an optional criteria string,
    return a list of matching roll numbers in their original order:
    - None: all roll numbers
    - 'above_average': marks >= class mean
    - 'below_average': marks < class mean
    - 'fail': marks < 40
    - 'toppers': marks >= 90
    - Any other criteria string: return None
    Example:
    >>> get_roll_nos([('CS01', 92), ('CS02', 35), ('CS03', 73)], 'toppers')
    ['CS01']
    '''

    result = []

    if criteria is None:
        for item in data:
            result.append(item[0])
        return result

    if criteria not in  ['above_average', 'below_average', 'fail', 'toppers']:
        return None

    total = 0
    for item in data:
        total = total + item[1]
    average  = total / len(data)

    for item in data:
        if criteria == "above_average":
            if item[1]>=average:
                result.append(item[0])
        elif criteria == "below_average":
            if item[1]<average:
                result.append(item[0])
        elif criteria == "fail":
                if item[1]<40:
                    result.append(item[0])
        elif criteria == "toppers":
            if item[1]>=90:
                result.append(item[0])
    return result 

data = [('CS01', 92), ('CS02', 35), ('CS03', 73)]

print(get_roll_nos(data, 'toppers'))
print(get_roll_nos(data, 'fail'))
print(get_roll_nos(data, 'above_average'))
print(get_roll_nos(data, 'below_average'))
print(get_roll_nos(data))
print(get_roll_nos(data, 'invalid'))
    