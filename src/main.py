from availabilityManager.add import adder
from availabilityManager.view import viewer
from availabilityManager.update import updater_menu
from utils.clear import clear_screen

def menu():

    clear_screen()
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


def stockManipulMenu():

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
                # Logic for delete to be implemented
                pass
            case "4":
                clear_screen()
                return
            case _:
                print("Invalid option. Please try a valid one")
                continue

def viewSercMenu():

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
                # Logic for search stock to be implemented
                pass
            case "3":
                clear_screen()
                return
            case _:
                print("Invalid option. Please try a valid one")
                continue

if __name__ == "__main__":
    menu()