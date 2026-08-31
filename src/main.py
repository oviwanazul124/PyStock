from stockManage.adder import adder

def menu():
    while True:
        print("PyStock System")
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
                menu()


def stockManipulMenu():
    print("PyStock System - Stock Manipulation")
    print("1. Add Stock")
    print("2. Update Stock")
    print("3. Delete Stock")
    print("4. Back to Main Menu")

    opt = input("Select an option: ")

    match opt:
        case "1":
            adder()
        case "2":
            # Logic for update to be implemented
            pass
        case "3":
            # Logic for delete to be implemented
            pass
        case "4":
            menu()
        case _:
            print("Invalid option. Please try a valid one")
            stockManipulMenu()

def viewSercMenu():
    print("PyStock System - View/Search Stock")
    print("1. View All Stock")
    print("2. Search Stock")
    print("3. Back to Main Menu")

    opt = input("Select an option: ")

    match opt:
        case "1":
            # Logic for view all stock to be implemented
            pass
        case "2":
            # Logic for search stock to be implemented
            pass
        case "3":
            menu()
        case _:
            print("Invalid option. Please try a valid one")
            viewSercMenu()

if __name__ == "__main__":
    menu()