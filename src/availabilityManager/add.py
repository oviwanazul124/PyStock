from saveManager.save import save_item, item_exists
from utils.validator import is_price_correct, is_stock_correct
from utils.clear import clear_screen
from time import sleep as wait


def adder():

    # Start the validation process for the items to be added.
    item_name, item_price, item_stock = adder_validation()

    # Save the item to the temporal save state.
    save_item(item_name, item_price, item_stock)

    # Confirm to the user the action was succesful and ask if they want to add more.
    print(f"The item {item_name}, has been added to the stock with a price of {item_price} and a current stock of {item_stock}.")
    print("Do you want to add another item? (y/n)")
    opt = input("")
    if opt.lower() == "y" or opt.lower() == "yes":
        adder()
    else:
        clear_screen()
        return

def adder_validation():
    # Validation for item name
    while True:
        clear_screen()
        print("PyStock System - Add Stock")
        print("-" * 30)
        item_name = input("Enter the item name:")
        if not item_name:
            print("Please enter a valid item name. It shouldn't be empty or anything that isn't a text.")
            continue
        elif item_exists(item_name):
            print("The item name already exists. Please enter a different item name.")
            continue
        else:
            break

    # Validation for item price
    while True:
        item_price = input("Enter the item price: ")
        try:
            item_price = float(item_price)
            if is_price_correct(item_price) == False:
                print("Please enter a valid item price. It should be a positive number that isn't 0.")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid item price. It should be a number that isn't a text or any other character. The number must be written like '19.00'")

    # Validation for stock
    while True:
        item_stock = input("Enter the item stock: ")
        try:
            item_stock = int(item_stock)
            if is_stock_correct(item_stock) == False:
                print("Please enter a valid item stock. It should be a positive number.")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid item stock. It should be a number that isn't a text or any other character.")

    return item_name, item_price, item_stock