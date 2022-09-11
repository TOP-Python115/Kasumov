from math import sqrt

class Point:
    """Координты точки"""
    def __init__(self, *args: int):
      for i in args:
        if i < 0:
          raise ValueError('Не принимаются координаты меньше нуля')
        else:
         self.x = args[0]
         self.y = args[1]

        

class LineSegment:

    def __init__(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.F = F
        self.G = G
      
    def r(self, a, b, c, d ):
      """Расчет сторон многоугольника"""
      return sqrt((a - b) ** 2 + (c - d) ** 2)

    
    def sides(self):
      """Расчет сторон многоугольника"""
      side1 = self.r(self.B.x, self.A.x, self.B.y, self.A.y)
      side2 = self.r(self.C.x, self.B.x, self.C.y, self.B.y)
      side3 = self.r(self.D.x, self.C.x, self.D.y, self.C.y)
      side4 = self.r(self.E.x, self.D.x, self.E.y, self.D.y)
      side5 = self.r(self.F.x, self.E.x, self.F.y, self.E.y)
      side6 = self.r(self.G.x, self.F.x, self.G.y, self.F.y)
      side7 = self.r(self.A.x, self.G.x, self.A.y, self.G.y)
      return side1,side2,side3,side4,side5,side6,side7 


class Polygon(LineSegment):
  """Периметр Многоугольника"""
  def perimetr(self):
    return sum(self.sides())
  



A = Point(0, 0)
B = Point(5, 2)
C = Point(4, 1)
D = Point(7, 3)
E = Point(7, 4)
F = Point(7, 5)
G = Point(8, 6)
pol = Polygon(A, B, C, D, E, F, G)
print(round(pol.perimetr(), 2))
    
