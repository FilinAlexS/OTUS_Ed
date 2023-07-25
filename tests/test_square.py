import pytest
from src.square import Square


@pytest.mark.parametrize('side, expected_perimeter, expected_area',
                         [
                             (12, 48, 144),
                             (1, 4, 1),
                             (4, 16, 16)
                         ]
                         )
def test_square_creation_positive(side, expected_area, expected_perimeter):
    square = Square(side)
    assert square.name == 'Square', 'Expected name is Square'
    assert square.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert square.get_area() == expected_area, 'Expected correct area'


@pytest.mark.parametrize('side', [0, -3], ids=['side is zero', 'side is negative'])
def test_square_creation_negative(side):
    with pytest.raises(ValueError):
        Square(side)


def test_two_square_areas_sum():
    expected_sum = 45
    square_1 = Square(3)
    square_2 = Square(6)
    assert square_1.add_area(square_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [3, 3.0, 'something'], ids=['int', 'float', 'str'])
def test_two_square_areas_sum_negative(some_other_class):
    square_1 = Square(7)
    with pytest.raises(ValueError):
        square_1.add_area(some_other_class)
