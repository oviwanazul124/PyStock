from stockManage.adder import adder
from viewerupdtManager.viewer import viewer
from viewerupdtManager.update import updater_menu

def menu():

    print("PyStock System")
    while True:
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

    print("PyStock System - Stock Manipulation")
    while True:
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
                return
            case _:
                print("Invalid option. Please try a valid one")
                continue

def viewSercMenu():

    print("PyStock System - View/Search Stock")
    while True:
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
                return
            case _:
                print("Invalid option. Please try a valid one")
                continue

if __name__ == "__main__":
    menu()