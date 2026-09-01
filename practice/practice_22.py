
def calculate_total_spent(filename):
    '''
    Args:
        filename (str): The path to the file containing transaction data.

    Returns:
        dict: A dictionary where keys are customer names and values are the total amount spent.
    '''
    totals = {}
    # open the file safely
    with open(filename, 'r') as file:
        # loop through each line in the file 
        for line in file:
            # skip any empty lines just in case
            if not line.strip():
                continue
            # clean the line and split into commas
            parts = line.strip().split(',')
            # extract the name and convert the amount to a float
            name = parts[0]
            amount = float(parts[1])

            # add the amount to the currentn total and round to 2 decimal places
            # .get(name, 0.0) safely fethches the current or starts it at 0.0
            new_total = totals.get(name, 0.0) + amount
            totals[name] = round(new_total,2)
    # return the completed dictionary 
    return totals
print(calculate_total_spent('D:\Python Learning\practice\customer.txt'))