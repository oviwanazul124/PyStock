## Utils Imports

from utils.clear import clear_screen
from utils.confirmation_prompt import confirmation_prompt

## Models Imports

from models.type_prompt_mode import PromptMode

## Services Imports

from services.search_service import by_name, by_id, by_stock_or_price
from services.save_service import delete_item


def deleter_menu() -> None:
    """
    Function in charge of displaying the search menu and getting the user's choice.
    
        Returns:
            int: The user's choice.
    """

    clear_screen()
    print("PyStock - Delete Interface")
    print("-" * 30)
    print("1. Delete by Product")
    print("2. Delete by Price")
    print("3. Delete by Stock")
    print("4. Back to Main Menu")

    opt = input("Select an option: \n")

    match opt:
            case "1":
                while True:
                    print("Please enter 'ID' if you want to delete by ID or 'NAME' if you want to delete by name and using 'exit' to exit the delete")
                    opt = input("Select an option: \n").lower()

                    if opt == "id":
                        item = by_id()
                        if not _item_deletion(item):
                            return
                    elif opt == "name":
                        item = by_name()
                        if not _item_deletion(item):
                            return
                    elif opt == "exit":
                        return
                    else:
                        print("Invalid option. Please try a valid one \n")
                        continue
            case "2":
                item = by_stock_or_price("price")
                if not _item_deletion(item):
                    return
                pass

            case "3":
                item = by_stock_or_price("stock")
                if not _item_deletion(item):
                    return
                pass

            case "4":
                return

            case _:
                print("Invalid option. Please try a valid one \n")

def _item_deletion(item) -> bool:
    """
    Function in charge of handling the deletion of an item after it has been searched for.
    
        Args:
            item: The item to be deleted.
        
        Returns:
            bool: True if the item was deleted, False otherwise.
        
        Raises:
            None
    """

    if item is None:
        print("No product found with the given criteria.")
        input("Press enter to continue...")
        return False

    if confirmation_prompt(PromptMode.DELETE_CONFIRM):
        delete_item(item)
        return True
    else:
        print("Deletion cancelled. \n")
        return False