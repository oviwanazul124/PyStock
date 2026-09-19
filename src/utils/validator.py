from saveManager.save import retrieve_item

def is_price_correct(price):
    """
    Validates if the given price is a positive number greater than zero.
    
        Args:
            price (float): The price to validate.
        
        Returns:
            bool: True if the price is valid False otherwise.
        
        Raises:
            ValueError: If the price is not a number.
    """

    try:
        price = float(price)

        if price <= 0:
            return False
        else:
            return True

    except ValueError:
        raise ValueError("Function is_price_correct: Has been called with a value that isn't a float")

def is_stock_correct(stock):
    """
    Validates if the given stock is a positive number greater than or equal to zero.

        Args:
            stock (int): The current stock of the product.
            new_stock (int): The new stock to validate.
        
        Returns:
            bool: True if the new stock is valid False otherwise.
        
        Raises:
            ValueError: If the stock is not a number.    
    """

    if stock < 0:
        return False
    else:
        return True

def is_product_same(id, new_product_name):
    """
    Validates if the given product name is the same as the current product name.

        Args:
            product (str): The current name of the product.
            new_product_name (str): The new name to compare with the current name of the product.
        
        Returns:
            bool: True if the new product name is the same as the current product name, False otherwise.
        
        Raises:
            TypeError: If the product does not exist in the added dictionary.
    """

    pr = retrieve_item(id)
    if pr == None:
        raise TypeError("Function is product_same: Has been called with a product that dosen't exists in the added dictionary")

    if pr.name == new_product_name:
        return True
    else:
        return False

def is_price_same(id, price):
    """
    Validates if the given price is the same as the current price of the product.
    
        Args:
            product (str): The name of the product to check.
            price (float): The price to compare with the current price of the product.
        
        Returns:
            bool: True if the price is the same as the current price of the product, False otherwise.
        
        Raises:
            TypeError: If the product does not exist in the added dictionary.
    """

    pr = retrieve_item(id)
    if pr == None:
        raise TypeError("Function is_price_same: Has been called with a product that doesn't exist in the added dictionary")

    if pr.price == price:
        return True
    else:
        return False

def is_stock_same(id, stock):
    """
    Validates if the given stock is the same as the current stock of the product.

        Args:
            product (str): The name of the product to check.
            stock (int): The stock to compare with the current stock of the product.
        
        Returns:
            bool: True if the stock is the same as the current stock of the product, False otherwise.

        Raises:
            TypeError: If the product does not exist in the added dictionary.


    """

    pr = retrieve_item(id)
    if pr == None:
        raise TypeError("Function is_stock_same: Has been called with a product that dosen't exists in the added dictionary")

    if pr.stock == stock:
        return True
    else:
        return False
