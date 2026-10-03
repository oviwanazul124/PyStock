## Import Models

from src.models.product import Product
from src.models.save_search_mode import search_mode
from src.models.custom_errors import ProductNotFoundError

added_items : dict[int, Product] = {}

def save_item(item_name : str, item_price : float, item_stock : int) -> None:
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

def delete_item(search_term : Product | list[Product]) -> None:
    """
    Function in charge of deleting an item from the added items dictionary.

        Args:
            search_term (Product | list[Product]): The item or list of items to be deleted.

        Returns:
            None

        Raises:
            None
    """

    if isinstance(search_term, Product):
        del added_items[search_term.id]
    elif isinstance(search_term, list):
        for product in search_term:
            del added_items[product.id]
    else:
        raise ValueError("Invalid search_term type. Must be a Product or a list of Products.")

def get_full_view() -> dict:
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

def update_name(search_term : str, new_name : str, mode : search_mode) -> None:
    """
    Function in charge of updating the name of the items in the added items dictionary.

        Args:
            search_term (str): The name or id of the item to be updated.
            mode (search_mode): The mode of the search, either by name or by id.
        
        Returns:
            None
        
        Raises:
            ValueError: If the old name does not exist in the added items dictionary.
    """

    if mode == search_mode.NAME:
        product_id = _get_id_by_item(search_term)

    if product_id is None:
        raise ValueError("Function update_name: Has been called with a product that doesn't exist in the added dictionary")

    product_id = int(product_id)

    pr = added_items[product_id]
    pr.name = new_name



def retrieve_item(search_term : str, mode : search_mode) -> Product:
    """
    Function in charge of retrieving the item from the added items dictionary.

        Args:
            search_term (str): The name or id of the item to be retrieved.
            mode (search_mode): The mode of the search, either by name or by id.

        Returns:
            dict: The item's data.
        
        Raises:
            ValueError: If the item does not exist in the added dictionary.
    """

    if mode is search_mode.NAME:
        product_id = _get_id_by_item(search_term)
    else:
        product_id = int(search_term)

    if product_id is None:
        raise ValueError(f"{search_term} does not exist in the added dictionary, {mode.name} search mode")

    product_id = int(product_id)

    try:
        return added_items[product_id]
    except KeyError:
        raise ProductNotFoundError(f"Function retrieve_item: Has been called with a product that doesn't exist in the added dictionary. Product ID: {product_id}")



def item_exists(search_term : str, mode : search_mode) -> bool:
    """
    Function in charge of checking if the item exists in the added items dictionary.

        Args:
            search_term (str): The name or id of the item to be checked.
            mode (search_mode): The mode of the search, either by name or by id.

        Returns:
            bool: True if the item exists, False if the item does not exist.
        
        Raises:
            None
    """

    if mode is search_mode.NAME:
        term = _get_id_by_item(search_term)
    else:
        term = int(search_term)

    for id in added_items:
        if id == term:
            return True
    return False

def update_price(search_term : str , item_price : float, mode : search_mode) -> bool:
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

    if mode == search_mode.NAME:
        id = _get_id_by_item(search_term)

        if id is None:
            raise ProductNotFoundError(f"Function update_price: Has been called with a product that doesn't exist in the added dictionary. Product name: {search_term}")
    else:
        id = int(search_term)

    pr = added_items[id]
    pr.price = item_price

    return True

def update_stock(search_term : str, item_stock : int, mode : search_mode) -> bool:
    """
    Function in charge of updating the stock of the items in the added items dictionary.
    
        Args:
            search_term (str): The name or id of the item to be updated.
            item_stock (int): The new stock of the item.
            mode (search_mode): The mode of the search, either by name or by id.

        Returns:
            bool: True if the item was updated successfully.
        
        Raises:
            None
    """

    if mode is search_mode.NAME:
        id = _get_id_by_item(search_term)

        if id is None:
            raise ProductNotFoundError(f"Function update_stock: Has been called with a product that doesn't exist in the added dictionary. Product name: {search_term}")
    else:
        id = int(search_term)

    pr = added_items[id]
    pr.stock = item_stock

    return True

def _get_id_by_item(item_name : str) -> int | None:

    for id in added_items:
        if added_items[id].name == item_name:
            return id