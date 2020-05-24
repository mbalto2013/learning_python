class Color:
  def __init__(self, red, blue, green):
    self.red = red
    self.blue = blue
    self.green = green

  def __repr__(self):
    return "Color with RGB = ({red}, {blue}, {green})".format(red=self.red, blue=self.blue, green=self.green)

  def add(self, other):
    """
    Adds two RGB colors together
    Maximum value is 255
    """
    new_red = min(self.red + other.red, 255)
    new_blue = min(self.blue + other.blue, 255)
    new_green = min(self.green + other.green, 255)

    return Color(new_red, new_blue, new_green)

red = Color(255, 0, 0)
blue = Color(0, 255, 0)

magenta = red.add(blue)
print(magenta)
# Prints "Color with RGB = (255, 255, 0)"