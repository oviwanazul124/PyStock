# Services Import

from services.save_service import update_price, update_stock, item_exists, retrieve_item, update_name

# Model Import

from models.save_search_mode import search_mode
from models.type_prompt_mode import PromptMode

## Utils Import
from utils.clear import clear_screen
from utils.confirmation_prompt import confirmation_prompt
from utils.validator import is_price_correct, is_stock_correct

def update_product_info() -> None:
    """
    Function in charge of updating the product info (price and stock) of a product.

        Args:
            None
        
        Returns:
            None
        
        Raises:
            None
    """

    clear_screen()

    # Search Mode for the product

    opt = input("Do you want to search the product by name or by ID? (name/id): \n")

    if opt.lower() == "name":
        search = search_mode.NAME
        selected = "name"
    else:
        search = search_mode.ID
        selected = "ID"

    # Logic for checking if the product exists before updating.
    search_term = input(f"Enter the product {selected} to update: \n")
    

    if not item_exists(search_term, search):
        print("Product not found. Please try again. \n")
        return

    # Showing the current project info and asking what wants to change.
    pr = retrieve_item(search_term, search)

    if pr is None:
        raise ValueError("Product not found. Please try again. \n")

    while True:
        # Print to the screen the current info and ask what wants to change.
        print(f"The current info are: \n Price: {pr.price}\nStock: {pr.stock}\n")
        print("What do you want to change?")
        print("1. Price")
        print("2. Stock")
        print("3. Back to Update Menu")

        # Logic for implementing the changes to the product info.
        opt = input("Select an option:")

        # Logic for price change.
        match opt:
            case "1":

                while True:

                    # Logic for handling unexpected ValueError.
                    try:
                        new_price = float(input("Enter the new price: "))
                    except ValueError:
                        print("Please enter a valid item price that is a number.")
                        continue

                    # Validation of the price being a positive number that isn't 0.
                    if not is_price_correct(new_price):
                        print("Please enter a valid item price that is a positive number greater than 0.")
                        continue

                    # Logic for handling the same price change.
                    print(search)
                    if pr.is_price_same(new_price):
                        print("The new price is the same as the current price. Please enter a different price.")
                        continue

                    # Logic for updating the price and confirming the change to the user.
                    print(f"Price being updated to {new_price} \n")

                    # Logic stop cyclic loop between menus
                    if confirmation_prompt(PromptMode.UPDATE_CONFIRM) == False:
                        break 
                    update_price(search_term, new_price, search)

                    print("Price updated succesfully. \n")
                    if not confirmation_prompt(PromptMode.UPDATE_MORE_CONFIRM):
                        return
                    else:
                        break

            # Logic for stock change
            case "2":

                while True:

                    # Logic for handling unexpected ValueError.
                    try:
                        new_stock = int(input("Enter the new stock: "))
                    except ValueError:
                        print("Please enter a valid item stock that is a number.")
                        continue

                    # Logic for handling stock that is negative.
                    if is_stock_correct(new_stock) == False:
                        print("Please enter a valid item stock that is a positive number.")
                        continue

                    # Logic for handling the same stock change.
                    if pr.is_stock_same(new_stock):
                        print("The new stock is the same as the current stock. Please enter a different stock.")
                        continue

                    # Logic for updating the stock and confirming the change to the user.
                    print(f"Stock being updated to {new_stock} \n")

                    # Logic stop cyclic loop between menus
                    if confirmation_prompt(PromptMode.UPDATE_CONFIRM) == False:
                        break
                    update_stock(search_term, new_stock, mode=search)
                    print("Stock updated succesfully. \n")            
                    if not confirmation_prompt(PromptMode.UPDATE_MORE_CONFIRM):
                        return
                    else:
                        break

            case "3":
                return

            case _:
                print("Invalid option. Please try a valid one \n")

def update_product_name():
    """
    Function in charge of updating the product name of a product.

        Args:
            None
        
        Returns:
            None
        
        Raises:
            None
    """
    clear_screen()

    while True:

        mode = input("Do you want to search the product by name or by ID? (name/id): \n")

        if mode.lower() == "name":
            search = search_mode.NAME
            selected = "name"
        else:
            search = search_mode.ID
            selected = "ID"

        # Handling initial product input
        print("Please enter the product you want to rename: \n")
        search_term = input(f"Product {selected}: \n")

        # Verifying the product itself exists
        if not item_exists(search_term, search):
            print("Product not found. Please try again. \n")
            continue

        # Handling new product name
        print("Please enter the new name for the product: \n")
        new_product_name = input("New product name: \n")

        pr = retrieve_item(search_term, search)
        
        # Edge cases
        if pr.is_named_same(new_product_name):
            print("The new product name is the same as the current product name. Please enter a different name.")
            continue

        if item_exists(new_product_name, search):
            print("The new product name already exists. Please enter a different name.")
            continue

        # Renaming of the product itself
        if confirmation_prompt(PromptMode.UPDATE_CONFIRM) == False:
            break
        update_name(search_term, new_product_name, search)
        print(f"Product with {selected} {search_term} has been renamed to {new_product_name}. \n")
        break
    return

