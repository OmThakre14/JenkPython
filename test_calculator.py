# test_calculator.py

import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract():
    assert calculator.subtract(5, 2) == 3
    assert calculator.subtract(10, 5) == 5

def test_multiply():
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 5) == -10

def test_divide():
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(8, 4) == 2

def test_divide_by_zero():
    try:
        calculator.divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
    else:
        assert False, "Exception not raised"

    