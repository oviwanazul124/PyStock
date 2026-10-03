def is_price_correct(price : float) -> bool:
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
        return price > 0

    except ValueError:
        raise ValueError("Function is_price_correct: Has been called with a value that isn't a float")

def is_stock_correct(stock : int) -> bool:
    """
    Validates if the given stock is a positive number greater than or equal to zero.

        Args:
            stock (int): The current stock of the product.
        
        Returns:
            bool: True if the new stock is valid False otherwise.
        
        Raises:
            ValueError: If the stock is not a number.    
    """

    try:
        stock = int(stock)
        return stock >= 0

    except ValueError:
        raise ValueError("Function is_stock_correct: Has been called with a value that isn't an integer")

