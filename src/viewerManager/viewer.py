from saveManager.save import getData

def viewer():

    # Get current data from the save
    data = getData()

    # If data is empty show it via screen
    if len(data) == 0:
        print("No products has been added.")
        return

    # If not empty, show the data in a table format
    print(f"{'Product Name':<20} {'Price':<10} {'Stock':<10}")
    print("-" * 40)
    for product_name, product_info in data.items():
        print(f"{product_name:<20} {product_info['price']:<10} {product_info['stock']:<10}")
