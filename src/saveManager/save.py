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

def update_data(item_name, item_price=None, item_stock=None):
    """
    Function in charge of updating the items in the added items dictionary.

        Args:
            item_name (str): The name of the item to be updated.
            item_price (float, optional): The new price of the item. Defaults to None.
            item_stock (int, optional): The new stock of the item. Defaults to None.

        Returns:    
            None
        
        Raises:
            None
    """

    # Logic for implementing the changes to the item information.
    if item_price == None:
        added_items[item_name] = {
            "price": added_items[item_name]["price"],
            "stock": item_stock
            
        }
    else:
        added_items[item_name] = {
            "price": item_price,
            "stock": added_items[item_name]["stock"]
        }

def update_data_product(old_name, new_name):

    added_items[new_name] = {
        "price": added_items[old_name]["price"],
        "stock": added_items[old_name]["stock"]
    }

    if old_name in added_items:
        added_items[new_name] = added_items.pop(old_name)


def get_data():
    """
    Function in charge of returning the current items added

        Returns:
            dict: A dictionary containing the added items with their names as keys and ther price and stock as values.
    
    """
    return added_items