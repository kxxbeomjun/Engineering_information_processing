# -*- coding: utf-8 -*-
"""OOP2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/
"""

#OOP_part2 HW

import math
## __str__ overwriter
class Shape:
  def __init__(self,x,y):
    self.__x = x
    self.__y = y
  def getXYLoc(self):
    return (self.__x, self.__y)
  def setXYLoc(self,x, y):
    self.__x = x
    self.__y = y
  def calcArea(self):
    raise NotImplementedError("Method calcArea not implemented")
  def calcPerimeter(self):
    raise NotImplementedError("Method calcPerimeter not implemented")

class Circle(Shape):
  def __init__(self,x,y,r):
    Shape.__init__(self,x,y)
    self.__radius = r
  def calcArea(self):
    return math.pi * self.__radius ** 2
  def calcPerimeter(self):
    return 2 * math.pi * self.__radius  # perimeter of circle = 2*pi*r

class Square(Shape):
  def __init__(self,x,y,s):
    Shape.__init__(self,x, y)
    self.__size = s
  def calcArea(self):
    return self.__size ** 2
  def calcPerimeter(self):
    return self.__size * 4    # perimeter of square is 4 * one side's length

class Triangle(Shape):
  def __init__(self,x,y,s):
    Shape.__init__(self, x, y)
    self.__side = s
  def calcArea(self):
    return (self.__side ** 2) * math.sqrt(3)/4.0
  def calcPerimeter(self):
    return self.__side * 3    # perimeter of triangle is 3 * one side's length

shapes_list = (Circle(0,0,1),Circle(0,1,3),Square(0,0,4), Triangle(0,0,5))
total_area = 0
for shape in shapes_list:
  total_area += shape.calcArea()
print(total_area)

total_perimeter = 0
for shape in shapes_list:
  total_perimeter += shape.calcPerimeter()
print(total_perimeter)
