from math import sqrt

class Tetrahedron:
  """Кол - во ребер тетраэдра"""
  def __init__(self, ab, bc, ac, ad, bd, cd):
    self.ab = ab
    self.bc = bc
    self.ac = ac
    self.ad = ad
    self.bd = bd
    self.cd = cd
  """Формула высоты"""
  def height(self):
    h = sqrt((2 * self.ad) / 3)
    return h
  """Формула площади ребра""" 
  def square(self, a, b, c):
    item = (a + b + c) / 2
    per = sqrt(item * (item - a) * (item - b) * (item - c))
    return per
  """Формула площади тетраэдра"""
  def full_square(self):
    Rebro1 = self.square(self.ab, self.bc, self.ac)
    Rebro2 = self.square(self.ab, self.ad, self.bc)
    Rebro3 = self.square(self.bc, self.bd, self.cd)
    Rebro4 = self.square(self.ac, self.ad, self.cd)
    return (Rebro1 + Rebro2 + Rebro3 + Rebro4)
  """Формула объема тетраэдра"""
  def full_volume(self):
    return self.square(self.ab, self.bc, self.ac) * self.height()
    

    
t = Tetrahedron(4, 5, 6, 7, 8, 3) 

print(f"Площадь тетраэдра: {t.full_square()}")
print(f"Объем тетраэдра: {t.full_volume()}")