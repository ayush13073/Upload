class Shape:

  def area(self):
    print("Shape area")


class Square(Shape):

  def __init__(self, length):
    self.length = length

  def area(self):
    ans = self.length * self.length
    print("Square Area = %d" % ans)


class Circle(Shape):

  def __init__(self, radius):
    self.radius = radius

  def area(self):
    ans = 3.14159 * self.radius * self.radius
    print("Circle Area = %.2f" % ans)


# Create objects directly
s = Square(4)
c = Circle(3)

# Call methods directly
s.area()
c.area()