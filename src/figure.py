class Figure:

    def get_area(self):
        pass

    @property
    def area(self) -> None:
        print(self.get_area())

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return round(self.get_area() + figure.get_area(), 2)
        raise ValueError(f'Object {figure} is not subclass of Figure class')
