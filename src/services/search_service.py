## Utils Import

from utils.clear import clear_screen
from utils.data_manipulation import filter_by

# Models Import

from models.save_search_mode import search_mode
from models.product import Product

# Services Import

from services.save_service import retrieve_item


def by_name() -> Product | None:
    """
    Function in charge of searching for a product by its name. It prompts the user to enter a product name and retrieves the corresponding product from the database.

        Args:
            None

        Returns:
            Product | None: The product object if found, None otherwise.
        
        Raises:
            ValueError: If the product name is not found in the database.
    """

    clear_screen()
    while True:
        name = input("Enter the product name to search. If you want to exit, enter 'exit': \n")
        if name.lower() == 'exit':
            return
        
        item = retrieve_item(name, mode=search_mode.NAME)

        if item is None:
            print(f"No product found with the name '{name}'. Please try again.")
            continue

        return item

def by_id() -> Product | None:
    """
    Function in charge of searching for a product by its ID. It prompts the user to enter a product ID and retrieves the corresponding product from the database.
        Args:
            None
        Returns:
            Product | None: The product object if found, None otherwise.
        Raises:
            ValueError: If the product ID is not found in the database.
    """

    clear_screen()

    while True:
        search_term = input("Enter the product ID to search. If you want to exit, enter 'exit': \n")
        if search_term.lower() == 'exit':
            return

        item = retrieve_item(search_term, mode=search_mode.ID)

        if item is None:
            print(f"No product found with the ID '{search_term}'. Please try again.")
            continue
        return item

def by_stock_or_price(search_type : str) -> list[Product] | None:
    """
    Function in charge of searching for products by their stock or price. It prompts the user to enter a search criteria and retrieves the corresponding products from the database.
    
        Args:
            search_type (str): The type of search to perform. It can be either 'stock' or 'price'.    
        
        Returns:
            list[Product] | None: A list of product objects if found, None otherwise.
        
        Raises:
            ValueError: If the search type is not 'stock' or 'price'.
    """


    if search_type == "stock":
        string_set = ["EXACT_STOCK", "MIN_STOCK", "MAX_STOCK"]
    elif search_type == "price":
        string_set = ["EXACT_PRICE", "MIN_PRICE", "MAX_PRICE"]
    else:
        raise ValueError("Invalid type. Please use 'stock' or 'price'.")
        
    while True:
        clear_screen()
        print(f"Please enter '{string_set[0]}' if you want to search by exact {search_type}, '{string_set[1]}' if you want to search by minimum {search_type}, '{string_set[2]}' if you want to search by maximum {search_type} and using 'exit' to exit the search")
        opt = input("Select an option: \n").lower()

        if opt == string_set[0].lower():

            filtrer = input(f"Enter the exact {search_type} to search: \n")
            filtrer = int(filtrer)
            products = filter_by(mode=search_mode.EXACT, exact_filtrer=filtrer, type=search_type)

        elif opt == string_set[1].lower():

            filtrer = input(f"Enter the minimum {search_type} to search: \n")
            filtrer = int(filtrer)
            products = filter_by(mode=search_mode.MIN, min_filtrer=filtrer, type=search_type)

        elif opt == string_set[2].lower():

            filtrer = input(f"Enter the maximum {search_type} to search: \n")
            filtrer = int(filtrer)
            products = filter_by(mode=search_mode.MAX, max_filtrer=filtrer, type=search_type)

        elif opt == "exit":

            return
            
        else:
                        
            print("Invalid option. Please try a valid one \n")
            continue

        if len(products) == 0:
            print(f"No products found with the given {search_type} criteria. Please try again.")
            input("Press enter to continue...")
            continue
        else:
            return products
