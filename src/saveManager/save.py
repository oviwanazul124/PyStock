added_items = {}

def save_item(item_name, item_price, item_stock):
    """
    Function in charge of adding the items to the added items dictionary.

        Args:
            item_name (str): The name of the item to be added.
            item_price (float): The price of the item to be added.
            item_stock (int): The stock of the item to be added.
        
        Returns:
            None
        
        Raises:
            None
    """

    added_items[item_name] = {
        "price": item_price,
        "stock": item_stock
    }

def getData():
    """
    Function in charge of returning the current items added

        Returns:
            dict: A dictionary containing the added items with their names as keys and ther price and stock as values.
    
    """
    return added_items