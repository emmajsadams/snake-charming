# This is just a sample test for experiementing with Python class syntax. Has nothing todo with the flaskr package

class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def get_area(self): 
    return self.length * self.width

class Square(Rectangle):
  def __init__(self, length):
    Rectangle.__init__(self, length, length)

def test_rectangle_get_area():
  rectangle = Rectangle(4, 2)

  assert rectangle.get_area() == 8

def test_rectangle_length_width():
  rectangle = Rectangle(4, 2)

  assert rectangle.length == 4
  assert rectangle.width == 2

def test_square_get_area():
  square = Square(4)

  assert square.get_area() == 16

def test_square_length_width():
  square = Square(4)

  assert square.length == 4
  assert square.width == 4