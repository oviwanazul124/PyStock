from saveManager.save import get_data, update_data, update_data_product

data = get_data()

def updater_menu():
    print("PyStock System - Update Stock")
    print("Please enter the option you want to do with the item:")
    print("1. Update related info (Price, Stock)")
    print("2. Update product name")
    print("3. Back to Main Menu")

    opt = input("Select an option:  \n")

    match opt:
        case "1":
            update_product_info()
            pass
        case "2":
            update_product_name()
            pass
        case "3":
            return
        case _:
            print("Invalid option. Please try a valid one \n")

def confirmation_prompt(opt):
    """
    
    Function in charge of asking the user idfferent confirmation prompts depending on the option selected. '1' for updating related and '2' for wanting to update more products

        Args:
            opt (str): The option selected by the user.
        
        Returns:
            bool: False if user dosen't want to update more products. Only when option 1 is selected. Otherwise, it returns None.
        
        Raises:
            None
            
    """

    match opt:
        case "1":
            while True:
                confirmation = input("Are you sure you want to update this product? (y/n): \n")
                if confirmation.lower() == 'y':
                    break
                elif confirmation.lower() == 'n':
                    print("Update cancelled. \n")
                    return False
                else:
                    print("Invalid input. Please enter 'y' or 'n'. \n")            
        case "2":
            while True:
                confirmation = input("You want to update more products? (y/n):  \n")
                if confirmation.lower() == 'y':
                    update_product_info()
                elif confirmation.lower() == 'n':
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'. \n")
        case _:
            raise ValueError("confirmation_prompt() received an invalid option. Please select a valid option.")
        
def update_product_info():

    # Logic for checking if the product exists before updating.
    product_name = input("Enter the product name to update: \n")

    active_products = []
    for key in data.keys():
        active_products.append(key)
    if product_name not in active_products:
        print("Product not found. Please try again.")
        return

    # Showing the current project info and asking what wants to change.
    product_info = data[product_name]
    while True:

        # Print to the screen the current info and ask what wants to change.
        print(f"The current info are: \n Price: {product_info['price']}\nStock: {product_info['stock']}\n")
        print("What do you want to change?")
        print("1. Price")
        print("2. Stock")

        # Logic for implementing the changes to the product info.
        opt = input("Select an option:")

        # Logic for price change.
        if opt == "1":

            while True:

                # Logic for handling unexpected ValueError.
                try:
                    new_price = float(input("Enter the new price: "))
                except ValueError:
                    print("Please enter a valid item price that is a number.")
                    continue

                # Logic for handling prices that are 0 or negative.
                if new_price <= 0:
                    print("Please enter a valid item price that is a positive number that isn't 0.")
                    continue

                # Logic for handling the same price change.
                if new_price == product_info['price']:
                    print("The new price is the same as the current price. Please enter a different price.")
                    continue

                # Logic for updating the price and confirming the change to the user.
                product_info['price'] = new_price
                print(f"Price being updated to {new_price} \n")

                # Logic stop cyclic loop between menus
                if confirmation_prompt("1") == False:
                    break
                update_data(product_name, item_price=new_price)
                print("Price updated succesfully. \n")
                confirmation_prompt("2")
                break
            break

        # Logic for stock change
        elif opt == "2":

            while True:

                # Logic for handling unexpected ValueError.
                try:
                    new_stock = int(input("Enter the new stock: "))
                except ValueError:
                    print("Please enter a valid item stock that is a number.")
                    continue

                # Logic for handling stock that is negative.
                if new_stock < 0:
                    print("Please enter a valid item stock that is a positive number.")
                    continue

                # Logic for handling the same stock change.
                if new_stock == product_info['stock']:
                    print("The new stock is the same as the current stock. Please enter a different stock.")
                    continue

                # Logic for updating the stock and confirming the change to the user.
                product_info['stock'] = new_stock
                print(f"Stock being updated to {new_stock} \n")

                # Logic stop cyclic loop between menus
                if confirmation_prompt("1") == False:
                    break
                update_data(product_name, item_stock=new_stock) 
                print("Stock updated succesfully. \n")            
                confirmation_prompt("2")
                break
            break

def update_product_name():


    while True:
        # Handling initial product input
        print("Please enter the product you want to rename: \n")
        product_name = input("Product name: \n")

        # Verifying the product itself exists
        active_products = []
        for key in data.keys():
            active_products.append(key)
        if product_name not in active_products:
            print("Product not found. Please try again.")
            return
        
        # Handling new product name
        print("Please enter the new name for the product: \n")
        new_product_name = input("New product name: \n")

        # Edge cases
        if product_name == new_product_name:
            print("The new product name is the same as the current product name. Please enter a different name.")
            continue
        if new_product_name in active_products:
            print("The new product name already exists. Please enter a different name.")
            continue

        # Renaming of the product itself
        if confirmation_prompt("1") == False:
            break
        update_data_product(product_name, new_product_name)
        print(f"Product with name {product_name} has been renamed to {new_product_name}. \n")
        break
    return
