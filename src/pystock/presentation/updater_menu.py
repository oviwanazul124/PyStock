## Utils import

from utils.clear import clear_screen

## Services Import

from services.update_service import update_product_info, update_product_name

def updater_menu() -> None:
    """
    Function in charge of showing the menu for the user and handle the option that he select himself.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    # Handle menu show to the CLI.
    while True:
        clear_screen()
        print("PyStock System - Update Stock")
        print("-" * 30)
        print("Please enter the option you want to do with the item:")
        print("1. Update related info (Price, Stock)")
        print("2. Update product name")
        print("3. Back to Main Menu")

        opt = input("Select an option:  \n")

        # Logic about the option selected by the user.
        match opt:
            case "1":
                update_product_info()
            case "2":
                update_product_name()
            case "3":
                return
            case _:
                print("Invalid option. Please try a valid one \n")