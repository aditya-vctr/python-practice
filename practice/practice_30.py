# Shopping List
def process_grocery_list(grocery_list:list, request:str):
    """Process the grocery list as per the request.

    Args:
        grocery_list (list[dict]) - A list of dictionary with the keys
            "name", "quantity" and "price", where "price" is the amount of 
            one unit of the item.
        request: (str) - A string containing one of the following request.
            - 'total_bill_amount'
            - 'max_quantity_item'
            - 'sort_by_total_amount'

    Returns: 
        The output corresponding to the request.
    """
    # REQUEST 1: Calculate the total bill
    if request == 'total_bill_amount':
        total = 0
        # loop through every dictionary in the list
        for item in grocery_list:
            # Mulitply price by quantity and add it to our running total
            item_total = item['price'] * item['quantity']
            total = total + item_total
        return total
    # REQUEST 2: Find the item with the highest quantity

    elif request == 'max_quantity_item':
        max_qty = -1
        best_item_name = ""

        for item in grocery_list:
            if item['quantity'] > max_qty:
                max_qty = item['quantity']
                best_item_name = item['name']
        return best_item_name

    # REQUEST 3: Sort by highest total amount,then by name
    elif request == 'sort_by_total_amount':
        sorted_list = sorted(grocery_list, key=lambda x: (-(x['price'] * x['quantity']), x['name']))
        return sorted_list