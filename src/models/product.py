from math import isclose

class Product:

    counter = 1

    def __init__(self, name : str, price : str | float, stock : int | str) -> None:
        self.name = name
        self.price = float(price)
        self.stock = int(stock)
        self.id = Product.counter
        Product.counter += 1

    def is_price_same(self, price : float) -> bool:
        """
        Checks if the given price is the same as the product's current price.

            Args:
                price (float): The price to compare with the product's current price.
            
            Returns:
                bool: True if the prices are the same, False otherwise.
        """

        return isclose(self.price, price)

    def is_stock_same(self, stock : int) -> bool:
        """
        Checks if the given stock is the same as the product's current stock.

            Args:
                stock (int): The stock to compare with the self stock.

            Returns:
                bool: True if the stocks are the same, False otherwise.
        """

        return self.stock == stock

    def is_named_same(self, new_product_name : str) -> bool:
        """
        Checks if the given product name is the same as the product's current name.

            Args:
                new_product_name (str): The product name to compare with the self name.
            
            Returns:
                bool: True if the names are the same, False otherwise.
        """

        return self.name == new_product_name