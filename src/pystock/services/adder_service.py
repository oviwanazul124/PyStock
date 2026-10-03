## Import Utils
from pystock.utils.validator import is_price_correct, is_stock_correct
from pystock.utils.clear import clear_screen

## Import Services
from pystock.services.save_service import item_exists

## Models Import
from pystock.models.save_search_mode import search_mode

def adder_validation() -> tuple[str, float, int]:
    """
    Returns a tuple containing the validated item name, price, and stock after prompting the user for input.

        Args:
            None

        Returns:
            tuple[str, float, int]: A tuple containing the validated item name, price, and stock.
        
        Raises:
            ValueError: If the item name is empty or already exists, or if the price or stock is invalid.
    
    """ 
    # Validation for item name
    while True:
        clear_screen()
        print("PyStock System - Add Stock")
        print("-" * 30)
        item_name = input("Enter the item name:")
        
        if not item_name:
            print("Please enter a valid item name. It shouldn't be empty or anything that isn't a text.")
            continue
        elif item_exists(item_name, search_mode.NAME):
            print("The item name already exists. Please enter a different item name.")
            continue
        else:
            break

    # Validation for item price
    while True:
        item_price = input("Enter the item price: ")
        try:
            item_price = float(item_price)
            if not is_price_correct(item_price):
                print("Please enter a valid item price. It should be a positive number that isn't 0.")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid item price. It should be a number that isn't a text or any other character. The number must be written like '19.00'")

    # Validation for stock
    while True:
        item_stock = input("Enter the item stock: ")
        try:
            item_stock = int(item_stock)
            if not is_stock_correct(item_stock):
                print("Please enter a valid item stock. It should be a positive number.")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid item stock. It should be a number that isn't a text or any other character.")

    return item_name, item_price, item_stock