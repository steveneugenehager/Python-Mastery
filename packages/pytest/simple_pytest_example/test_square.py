# Intended to be executed via pytest
 
from example_module import square

def main():
    test_square()


def test_square():
    assert square(2) == 4
    assert square(0) == 0
    assert square(8) == 64
    assert square(-8) == 64
    assert square(3) == 9

         
if __name__ == '__main__':
    main()