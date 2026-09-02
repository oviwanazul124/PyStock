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

def get_full_view():
    """
    Function in charge of returning the full view of the added items.

        Args:
            None

        Returns:
            tuple: The full view of the added items.

        Raises:
            None
    """

    snapshot = added_items.copy()

    for product_name, product_info in snapshot.items():
        snapshot[product_name] = (product_info["price"], product_info["stock"])

    snapshot = tuple(snapshot.items())

    return snapshot

def update_name(old_name, new_name):
    """
    Function in charge of updating the name of the items in the added items dictionary.

        Args:
            old_name (str): The old name of the item to be updated.
            new_name (str): The new name of the item to be updated.
        
        Returns:
            None
        
        Raises:
            ValueError: If the old name does not exist in the added items dictionary.
    """


    new_key = {
        
        "price": added_items[old_name]["price"],
        "stock": added_items[old_name]["stock"]
    }

    del added_items[old_name]
    added_items[new_name] = new_key


def retrieve_item(item_name):
    """
    Function in charge of retrieving the item from the added items dictionary.

        Args:
            item_name (str): The name of the item to be retrieved.
        
        Returns:
            dict: The item's data.
        
        Raises:
            ValueError: If the item does not exist in the added dictionary.
    """

    if item_name in added_items:
        current_item = added_items[item_name].copy()
        return current_item
    else:
        raise ValueError(f"Item {item_name} does not exist in the added dictionary.")

def item_exists(item_name):
    """
    Function in charge of checking if the item exists in the added items dictionary.

        Args:
            item_name (str): The name of the item to be checked.
        
        Returns:
            bool: True if the item exists, False if the item does not exist.
        
        Raises:
            None
    """

    if item_name in added_items:
        return True
    else:
        return False

def update_price(item_name, item_price):
    """
    Function in charge of updating the price of the items in the added items dictionary.
    
        Args:
            item_name (str): The name of the item to be updated.
            item_price (float): The new price of the item.
        
        Returns:
            bool: True if the item was updated successfully.
        
        Raises:
            None
    """

    added_items[item_name]["price"] = item_price

    return True

def update_stock(item_name, item_stock):
    """
    Function in charge of updating the stock of the items in the added items dictionary.
    
        Args:
            item_name (str): The name of the item to be updated.
            item_stock (int): The new stock of the item.
        
        Returns:
            bool: True if the item was updated successfully.
        
        Raises:
            None
    """

    added_items[item_name]["stock"] = item_stock

    return True
