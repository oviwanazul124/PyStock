from saveManager.save import save_item

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
        print("Returning to the stock manipulation menu...")
        return

def adder_validation():
    print("PyStock System - Add Stock")

    # Validation for item name
    while True:
        item_name = input("Enter the item name:")
        if not item_name:
            print("Please enter a valid item name. It shouldn't be empty or anything that isn't a text.")
            continue
        else:
            break

    # Validation for item price
    while True:
        item_price = input("Enter the item price: ")
        try:
            item_price = float(item_price)
            if item_price <= 0:
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
            if item_stock < 0:
                print("Please enter a valid item stock. It should be a positive number.")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid item stock. It should be a number that isn't a text or any other character.")

    return item_name, item_price, item_stock