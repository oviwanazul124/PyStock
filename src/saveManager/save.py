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
    return added_items