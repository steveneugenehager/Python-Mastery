# Intended to be executed via pytest
 
from example_module import square

def main():
    test_square()


def test_square_zero():
    assert square(0) == 0

def test_square_positive():
    assert square(2) == 4
    assert square(8) == 64

def test_square_negative():
    assert square(-3) == 9
    assert square(-8) == 64

         
if __name__ == '__main__':
    main()