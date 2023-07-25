import pytest
from src.rectangle import Rectangle


@pytest.mark.parametrize('side_a, side_b, expected_perimeter, expected_area',
                         [
                             (2, 3, 10, 6),
                             (10, 8, 36, 80),
                             (12, 14, 52, 168)
                         ]
                         )
def test_rectangle_create_pozitive(side_a, side_b, expected_perimeter, expected_area):
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.name == 'Rectangle', 'Expected name is Rectangle'
    assert rectangle.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert rectangle.get_area() == expected_area, 'Expected correct area'


@pytest.mark.parametrize('side_a, side_b',
                         [
                             (5, 0),
                             (-4, 4)
                         ],
                         ids=[
                             'one side is zero',
                             'one side is negative'
                         ])
def test_rectangle_create_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


def test_two_rectangle_areas_sum():
    expected_sum = 31
    rectangle_1 = Rectangle(3, 5)
    rectangle_2 = Rectangle(8, 2)
    assert rectangle_1.add_area(rectangle_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [6, 6.0, 'something'], ids=['int', 'float', 'str'])
def test_two_rectangle_areas_sum_negative(some_other_class):
    rectangle_1 = Rectangle(2, 5)
    with pytest.raises(ValueError):
        rectangle_1.add_area(some_other_class)
