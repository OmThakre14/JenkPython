# test_calculator.py

import Calculator

def test_add():
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0

def test_subtract():
    assert Calculator.subtract(5, 2) == 3
    assert Calculator.subtract(10, 5) == 5

def test_multiply():
    assert Calculator.multiply(3, 4) == 12
    assert Calculator.multiply(-2, 5) == -10

def test_divide():
    assert Calculator.divide(10, 2) == 5
    assert Calculator.divide(8, 4) == 2

def test_divide_by_zero():
    try:
        Calculator.divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
    else:
        assert False, "Exception not raised"

    