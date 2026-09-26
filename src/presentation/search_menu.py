## Utils Import

from utils.clear import clear_screen

## Services Import

from services.search_service import by_name, by_id, by_stock_or_price


def search_menu() -> None:
    """
    Function in charge of displaying the search menu and getting the user's choice.
    
        Returns:
            int: The user's choice.
    """

    clear_screen()
    print("PyStock - Search Interface")
    print("-" * 30)
    print("1. Search by Product")
    print("2. Search by Price")
    print("3. Search by Stock")
    print("4. Back to Main Menu")

    opt = input("Select an option: \n")

    match opt:
            case "1":
                while True:
                    print("Please enter 'ID' if you want to search by ID or 'NAME' if you want to search by name and using 'exit' to exit the search")
                    opt = input("Select an option: \n").lower()

                    if opt == "id":
                        item = by_id()
                        output_view(item)
                    elif opt == "name":
                        item = by_name()
                        output_view(item)
                    elif opt == "exit":
                        return
                    else:
                        print("Invalid option. Please try a valid one \n")
                        continue
            case "2":
                item = by_stock_or_price("price")
                output_view(item)
                pass

            case "3":
                item = by_stock_or_price("stock")
                output_view(item)
                pass

            case "4":
                return

            case _:
                print("Invalid option. Please try a valid one \n")

def output_view(product) -> None:
    """
    Function in charge of displaying the product information in a formatted way.

        Args:
            product (Product | list[Product] | None): The product or list of products to display.
        
        Returns:
            None
        
        Raises:
            ValueError: If the product is not a Product or list of Products.
    """

    clear_screen()

    if product is None:
        print("No product found with the given criteria.")
        input("Press enter to continue...")
        return

    if type(product) is list:
        print(f"{"ID":<20} {'Product Name':<20} {'Price':<10} {'Stock':<10}")
        print("-" * 60)
        for pr in product:
            print(f"ID: {pr.id:<20} Name: {pr.name:<20} Price: {pr.price:<10} Stock: {pr.stock:<10}")
    else:
        pr = product
        print(f"{"ID":<20} {'Product Name':<20} {'Price':<10} {'Stock':<10}")
        print("-" * 60)
        print(f"ID: {pr.id:<20} Name: {pr.name:<20} Price: {pr.price:<10} Stock: {pr.stock:<10}")

    input("Press enter to continue...")