from src.services.adder_service import adder_validation

def test_adder_validation(monkeypatch):
    # Mock inputs for item name, price, and stock
    inputs = iter(["Test Item", "10.0", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call the adder_validation function
    result = adder_validation()

    # Assert the returned values
    assert result == ("Test Item", 10.0, 5)