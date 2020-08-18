class Rectangle:
  #Initialize Rectangle object with height and width
  def __init__(self, w, h):
    self.width = w
    self.height = h
  #Change width of Rectangle
  def set_width(self, w):
    self.width = w
  #Change height of Rectangle
  def set_height(self, h):
    self.height = h
  #Returns area of Rectangle
  def get_area(self):
    area = (self.width * self.height)
    return(area)
  #Returns perimeter of Rectangle
  def get_perimeter(self):
    pm = (self.width * 2) + (self.height * 2)
    return(pm)
  #Returns diagonal of Rectangle
  def get_diagonal(self):
    diag = ((self.width ** 2) + (self.height ** 2)) ** .5
    return(diag)
  #Returns a string that represents Rectangle using "*"
  def get_picture(self):
    output = ""
    if (self.width > 50) or (self.height > 50):
      return("Too big for picture.")
    else:
      for row in range(self.height):
        line = (self.width * "*")
        output += line + "\n"
      return(output)
  #Returns the number of times another given shape can fit inside Rectangle without rotation
  def get_amount_inside(self, shape):
    outerWidth, outerHeight = self.width, self.height
    innerWidth, innerHeight = shape.width, shape.height
    widthX = int (outerWidth / innerWidth)
    heightX = int (outerHeight / innerHeight)
    return(widthX * heightX)
  #Returns Rectangle in string format
  def __str__(self):
    output = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    return(output)

class Square(Rectangle):
  #Initializes Square object with height and width being equal
  def __init__(self, size):
    self.width = size
    self.height = size
  #Change width (and height) of Square
  def set_width(self, w):
    self.width = w
    self.height = w
  #Change height (and width) of Square
  def set_height(self, h):
    self.height = h
    self.width = h  
  #Change size of Square
  def set_side(self, size):
    self.width = size
    self.height = size  
  #Returns Square in string format
  def __str__(self):
    output = "Square(side=" + str(self.width) + ")"
    return(output)