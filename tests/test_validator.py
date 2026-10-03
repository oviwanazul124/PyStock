from src.utils.validator import is_price_correct, is_stock_correct

def test_is_price_correct():

    assert is_price_correct(10.0) == True
    assert is_price_correct(0.01) == True
    assert is_price_correct(-5.0) == False
    assert is_price_correct(0.0) == False

    try:
        is_price_correct("invalid")
    except ValueError as e:
        assert str(e) == "Function is_price_correct: Has been called with a value that isn't a float"

def test_is_stock_correct():

    assert is_stock_correct(10) == True
    assert is_stock_correct(0) == True
    assert is_stock_correct(-5) == False

    try:
        is_stock_correct("invalid")
    except ValueError as e:
        assert str(e) == "Function is_stock_correct: Has been called with a value that isn't an integer"
        