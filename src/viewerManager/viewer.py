from saveManager.save import getData

def viewer():
    data = getData()
    if len(data) == 0:
        print("No products has been added.")
        return

    print(f"{'Product Name':<20} {'Price':<10} {'Stock':<10}")
    print("-" * 40)
    for product_name, product_info in data.items():
        print(f"{product_name:<20} {product_info['price']:<10} {product_info['stock']:<10}")
