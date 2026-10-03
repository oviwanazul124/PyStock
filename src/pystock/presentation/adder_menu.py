
## Services Imports

from services.save_service import save_item
from services.adder_service import adder_validation

## Utils Imports

from utils.clear import clear_screen
from utils.confirmation_prompt import confirmation_prompt

## Models Imports

from models.type_prompt_mode import PromptMode


def adder() -> None:
    """
    Function in charge of displaying the adder menu and getting the user's choice.
    
        Args:
            None

        Returns:
            None

        Raises:
            None
    """


    # Start the validation process for the items to be added.
    item_name, item_price, item_stock = adder_validation()

    # Save the item to the temporal save state.
    save_item(item_name, item_price, item_stock)

    # Confirm to the user the action was succesful and ask if they want to add more.
    print(f"The item {item_name}, has been added to the stock with a price of {item_price} and a current stock of {item_stock}.")
    if confirmation_prompt(PromptMode.ADD_CONFIRM):
        adder()
    else:
        clear_screen()
        return