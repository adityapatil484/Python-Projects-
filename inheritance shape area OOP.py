class Shape:
   def __init__(self):
      self.color = (0,0,0)

   def __str(self):
      return("RGB colors set to ()".format(self.color))

class Rectangle(Shape):
   def __init__(self,w,h):
      Shape.__init__(self)
      self.width = w
      self.height = h
      
   def area(self):
      self.area = self.width * self.height
      return (self.area)
             
   def __str(self):
      return("Height and Widht of rectangle are {} and {} and colors are {}".format(self.height,self.widht,self.color))
             
class Square(Rectangle):
   def __init__(self,s):
      Rectangle.__init__(self,s,s)
      self.side = s

   def area(self):
      self.area = self.side**2
      return (self.area)

   def __str__(self):
      return ("Side of Square is {} and colors are {}".format(self.side,self.color))

r1 = Rectangle(10,5)
print("Area of r1 = ", r1.area())
print(r1)

s1 = Square(10)
print("Area of s1 =", s1.area())
print("sq data members :", s1.width, s1.height, s1.side, s1.color)
print(s1)
