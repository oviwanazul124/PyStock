## Import Services

from services.save_service import get_full_view

def viewer() -> None:
    """
    Function in charge of displaying the current products in the inventory.
        Args:
            None
        Returns:
            None
        Raises:
            None    
    """


    # Get current data from the save
    data = get_full_view()
    
    # If data is empty show it via screen
    if len(data) == 0:
        print("No products has been added.")
        return

    # If not empty, show the data in a table format
    print(f"{"ID":<20} {'Product Name':<10} {'Price':<10} {'Stock':<10}")
    print("-" * 60)
    for id in data:
        pr = data[id]
        print(f"ID: {id:<20} Name: {pr.name:<10} Price: {pr.price:<10} Stock: {pr.stock:<10}")
    input("Press Enter to continue...")