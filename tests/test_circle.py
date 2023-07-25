import pytest
from src.circle import Circle


@pytest.mark.parametrize('radius, expected_perimeter, expected_area',
                         [
                             (1, 6.28, 3.14),
                             (7, 43.98, 153.94),
                             (22, 138.23, 1520.53)
                         ]
                         )
def test_circle_create_positive(radius,expected_perimeter, expected_area):
    circle = Circle(radius)
    assert circle.name == 'Circle', 'Expected name is Circle'
    assert circle.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert circle.get_area() == expected_area, 'Expected correct area'


@pytest.mark.parametrize('radius', (0, -2), ids=['radius is zero', 'radius is negative'])
def test_circle_creation_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)


def test_two_circle_areas_sum():
    expected_sum = 653.45
    circle_1 = Circle(12)
    circle_2 = Circle(8)
    assert circle_1.add_area(circle_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [15, 13.0, 'something'], ids=['integer', 'float', 'str'])
def test_two_circle_area_sum_negative(some_other_class):
    circle_1 = Circle(22)
    with pytest.raises(ValueError):
        circle_1.add_area(some_other_class)
