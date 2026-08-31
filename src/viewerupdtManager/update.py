from saveManager.save import get_data

data = get_data()

active_products = [product for product in data.keys()]

def updater_menu():
    print("PyStock System - Update Stock")
    print("Please enter the option you want to do with the item:")
    print("1. Update related info (Price, Stock)")
    print("2. Update product name")
    print("3. Back to Main Menu")

    opt = input("Select an option: ")

    match opt:
        case "1":
            # Logic for updating related info to be implemented
            pass
        case "2":
            # Logic for updating product name to be implemented
            pass
        case "3":
            return
        case _:
            print("Invalid option. Please try a valid one")

def confirmation_prompt(opt):
    """
    
    Function in charge of asking the user idfferent confirmation prompts depending on the option selected. '1' for updating related and '2' for wanting to update more products

        Args:
            opt (str): The option selected by the user.
        
        Returns:
            None

    """

    match opt:
        case "1":
            while True:
                confirmation = input("Are you sure you want to update this product? (y/n): ")
                if confirmation.lower() == 'y':
                    return
                elif confirmation.lower() == 'n':
                    print("Update cancelled. \n")
                    updater_menu()
                    return
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")            
        case "2":
            while True:
                confirmation = input("You want to update more products? (y/n): ")
                if confirmation.lower() == 'y':
                    update_product_info()
                elif confirmation.lower() == 'n':
                    print("Update cancelled. \n")
                    updater_menu()
                    return
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        

def update_product_info():

    # Logic for checking if the product exists before updating
    product_name = input("Enter the product name to update: ")
    if product_name not in active_products:
        print("Product not found. Please try again.")
        return

    # Showing the current project info and asking what wants to change
    product_info = data[product_name]
    while True:
        print(f"The current info are: \n Price: {product_info['price']}\nStock: {product_info['stock']}\n")
        print("What do you want to change?")
        print("1. Price")
        print("2. Stock")
        opt = input("Select an option:")
        if opt == "1":
            new_price = float(input("Enter the new price: "))
            product_info['price'] = new_price
            print(f"Price being updated to {new_price} \n")
            confirmation_prompt("1")
            print("Price updated succesfully. \n")
            confirmation_prompt("2")

        elif opt == "2":
            new_stock = int(input("Enter the new stock: "))
            product_info['stock'] = new_stock
            print(f"Stock updated to {new_stock}")
