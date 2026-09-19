from saveManager.save import get_full_view
from time import sleep as wait

def viewer():

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
    wait(5)