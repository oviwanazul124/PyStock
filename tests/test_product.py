from src.models.product import Product

def test_product_create():
    product = Product("Test Product", 10.0, 5)
    assert product.name == "Test Product"
    assert product.price == 10.0
    assert product.stock == 5
    assert product.id == 1

def test_product_id_increment():
    product1 = Product("Product 1", 5.0, 10)
    product2 = Product("Product 2", 15.0, 20)
    assert product1.id == 2
    assert product2.id == 3

def test_is_stock_same():
    product = Product("Test Product", 10.0, 5)
    assert product.is_stock_same(5) == True
    assert product.is_stock_same(10) == False

def test_is_named_same():
    product = Product("Test Product", 10.0, 5)
    assert product.is_named_same("Test Product") == True
    assert product.is_named_same("Another Product") == False

def test_is_price_same():
    product = Product("Test Product", 10.0, 5)
    assert product.is_price_same(10.0) == True
    assert product.is_price_same(9.99) == False