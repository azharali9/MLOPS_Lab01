from calculator import Calculator

def test_add():
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5

def test_subtract():
    calc = Calculator()
    result = calc.subtract(5, 3)
    assert result == 2

def test_add_negative():
    calc = Calculator()
    result = calc.add(-2, 3)
    assert result == 1
def test_multiply():
    calc = Calculator()
    result = calc.multiply(3,2)
    assert result == 6

# Run the tests
if __name__ == '__main__':
    test_add()
    test_subtract()
    test_add_negative()
    
    print("All tests passed!")
