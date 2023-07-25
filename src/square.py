from src.figure import Figure


class Square(Figure):

    def __init__(self, side: int):
        self.name = "Square"
        self.side = side
        self.check_create_square(side)

    def get_area(self) -> int:
        return self.side ** 2

    def get_perimeter(self) -> int:
        return self.side * 4

    @staticmethod
    def check_create_square(side):
        if not (side > 0):
            raise ValueError(f'Sides must be greater then 0. Got: {side}')
