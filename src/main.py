## Imports from Presentation

from presentation.adder_menu import adder
from presentation.updater_menu import updater_menu
from presentation.search_menu import search_menu
from presentation.deleter_menu import deleter_menu

## Imports from Services

from presentation.viewer_menu import viewer

## Imports from Utils

from utils.clear import clear_screen

def menu() -> None:
    """
    Function in charge of showing the main menu of the app

        Args:
            None

        Returns:
            None

        Raises:
            None
            
    """

    # Clear the screen before display menu
    clear_screen()

    # Main Menu Loop
    while True:
        print("PyStock System")
        print("-" * 30)
        print("1. Add/Update/Delete Stock")
        print("2. View/Search Stock")
        print("3. Exit")

        opt = input("Select an option: ")

        match opt:
            case "1":
                stockManipulMenu()
            case "2":
                viewSercMenu()
                pass
            case "3":
                print("Exiting the program...")
                exit()
            case _:
                print("Invalid option. Please try a valid one")
                continue


def stockManipulMenu() -> None:
    """
    Function in charge of showing the stock manipulation menu

        Args:
            None

        Returns:
            None

        Raises:
            None
    """

    # Main Loop for the stock manipulation menu
    while True:
        clear_screen()
        print("PyStock System - Stock Manipulation")
        print("-" * 30)
        print("1. Add Stock")
        print("2. Update Stock")
        print("3. Delete Stock")
        print("4. Back to Main Menu")

        opt = input("Select an option: ")

        match opt:
            case "1":
                adder()
            case "2":
                updater_menu()
                pass
            case "3":
                deleter_menu()
                pass
            case "4":
                clear_screen()
                return
            case _:
                print("Invalid option. Please try a valid one")
                continue

def viewSercMenu():
    """
    Function in charge of showing the view/search menu

        Args:
            None

        Returns:
            None

        Raises:
            None
    """

    # Main Loop for the view/search menu
    while True:
        clear_screen()
        print("PyStock System - View/Search Stock")
        print("-" * 30)
        print("1. View All Stock")
        print("2. Search Stock")
        print("3. Back to Main Menu")

        opt = input("Select an option: ")

        match opt:
            case "1":
                viewer()
                pass
            case "2":
                search_menu()
                pass
            case "3":
                clear_screen()
                return
            case _:
                print("Invalid option. Please try a valid one")
                continue

if __name__ == "__main__":
    menu()