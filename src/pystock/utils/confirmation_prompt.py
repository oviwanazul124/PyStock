from pystock.models.type_prompt_mode import PromptMode

def confirmation_prompt(type_prompt : PromptMode) -> bool | None:
    """
    Function in charge of asking the user idfferent confirmation prompts depending on the option selected. '1' for updating related and '2' for wanting to update more products

        Args:
            type_prompt (PromptMode): The type of confirmation prompt to display.
        
        Returns:
            bool: True if the user confirms the action, False otherwise.
        
        Raises:
            ValueError: If the option where the fuction was called is invalid     
    """

    # Logic for handling the prompt depending on the context of the action.
    match type_prompt:

        # Case confirmation of update to the product
        case PromptMode.UPDATE_CONFIRM:
            while True:
                confirmation = input("Are you sure you want to update this product? (y/n): \n")
                if confirmation.lower() == 'y':
                    break
                elif confirmation.lower() == 'n':
                    print("Update cancelled. \n")
                    return False
                else:
                    print("Invalid input. Please enter 'y' or 'n'. \n")            

        # Case confirmation of updating more products.
        case PromptMode.UPDATE_MORE_CONFIRM:
            while True:
                confirmation = input("You want to update more products? (y/n):  \n")
                if confirmation.lower() == 'y':
                    return True
                elif confirmation.lower() == 'n':
                    return False
                else:
                    print("Invalid input. Please enter 'y' or 'n'. \n")
        
        case PromptMode.DELETE_CONFIRM:
            while True:
                confirmation = input("Are you sure you want to delete this product? (y/n): \n")
                if confirmation.lower() == 'y':
                    return True
                elif confirmation.lower() == 'n':
                    print("Delete cancelled. \n")
                    return False
                else:
                    print("Invalid input. Please enter 'y' or 'n'. \n")

        case PromptMode.ADD_CONFIRM:
            while True:
                confirmation = input("Do you want to add another item? (y/n): \n")
                if confirmation.lower() == 'y':
                    return True
                elif confirmation.lower() == 'n':
                    return False
                else:
                    print("Invalid input. Please enter 'y' or 'n'. \n")
        case _:
            raise ValueError("confirmation_prompt() received an invalid option. Please select a valid option.")

        