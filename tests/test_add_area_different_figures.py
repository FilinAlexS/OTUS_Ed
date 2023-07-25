import pytest
from src.square import Square
from src.rectangle import Rectangle
from src.circle import Circle
from src.triangle import Triangle


@pytest.mark.parametrize('square_side, triangle_side_a, triangle_side_b, triangle_side_c, expected_sum_area',
                         [
                             (10, 13, 14, 15, 184),
                             (9, 4, 10, 7, 91.93),
                             (4, 16, 20, 15, 134.28)
                         ]
                         )
def test_add_area_square_triangle(square_side, triangle_side_a, triangle_side_b, triangle_side_c, expected_sum_area):
    square = Square(square_side)
    triangle = Triangle(triangle_side_a, triangle_side_b, triangle_side_c)
    assert triangle.add_area(square) == expected_sum_area


@pytest.mark.parametrize('circle_side, rectangle_side_a, rectangle_side_b, expected_sum_area',
                         [
                             (10, 13, 14, 496.16),
                             (9, 4, 10, 294.47),
                             (4, 16, 15, 290.27)
                         ]
                         )
def test_add_area_circle_rectangle(circle_side, rectangle_side_a, rectangle_side_b, expected_sum_area):
    circle = Circle(circle_side)
    rectangle = Rectangle(rectangle_side_a, rectangle_side_b)
    assert rectangle.add_area(circle) == expected_sum_area
