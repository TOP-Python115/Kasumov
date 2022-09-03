import sys
from abc import ABC


class Renderer(ABC):
    @property
    def what_to_render_as(self, name: str):
        return None


class VectorRenderer(Renderer):
    """Класс для создания векторных фигур"""
    def what_to_render_as(self, name: str):
        print(f'Drawing {name} as lines')


class RasterRenderer:
    """Класс для создания пиксельных фигур"""
    def what_to_render_as(self, name: str):
        print(f'Drawing {name} as pixels')


class Shape(ABC):
    def __init__(self):
        self.name = None


class Triangle(Shape):
    """Класс создающий треугольник,  в конструктор которого принимается класс Renderer """
    def __init__(self, renderer: Renderer):
        super().__init__()
        self.renderer = renderer
        self.name = 'Triangle'

    def create_shape(self):
        """Метод создающий треугольник определенного типа"""
        self.renderer.what_to_render_as(self.name)


class Square(Shape):
    """Класс создающий квадрат, в конструктор которого принимается класс Renderer """
    def __init__(self, renderer: Renderer):
        super().__init__()
        self.renderer = renderer
        self.name = 'Square'

    def create_shape(self):
        """Метод создающий треугольник определенного типа"""
        self.renderer.what_to_render_as(self.name)



sq = VectorRenderer()
tr = RasterRenderer()

triangle_raster = Triangle(tr)
triangle_vector = Triangle(sq)
square_raster = Square(tr)
square_vector = Square(sq)


print("To select the shape you need, type a number from 1 to 4")
inp = int(sys.stdin.readline())

if inp == 1:
    triangle_raster.create_shape()
elif inp == 2:
    triangle_vector.create_shape()
elif inp == 3:
    square_vector.create_shape()
elif inp == 4:
    square_raster.create_shape()