from models.product import Product

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

    pr = Product(item_name, item_price, item_stock)

    added_items[pr.id] = pr


def get_full_view():
    """
    Function in charge of returning the full view of the added items.

        Args:
            None

        Returns:
            dict: The full view of the added items.

        Raises:
            None
    """

    return added_items.copy()

def update_name(id, new_name):
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

    pr = added_items.get(id)

    pr.name = new_name

def retrieve_item(id):
    """
    Function in charge of retrieving the item from the added items dictionary.

        Args:
            item_name (str): The name of the item to be retrieved.
        
        Returns:
            dict: The item's data.
        
        Raises:
            ValueError: If the item does not exist in the added dictionary.
    """

    try:
        return added_items[int(id)]
    except KeyError:
        print(f"Item with ID {id} does not exist in the added items dictionary.")

def item_exists(id):
    """
    Function in charge of checking if the item exists in the added items dictionary.

        Args:
            item_name (str): The name of the item to be checked.
        
        Returns:
            bool: True if the item exists, False if the item does not exist.
        
        Raises:
            None
    """
    if int(id) in added_items:
        return True
    else:
        return False

def update_price(id, item_price):
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

    pr = added_items.get(int(id))

    pr.price = item_price

    return True

def update_stock(id, item_stock):
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

    pr = added_items.get(int(id))
    pr.stock = item_stock

    return True
