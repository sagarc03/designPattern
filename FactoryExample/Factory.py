from Shapes import Square, Rectangle, Circle

class Factory:
  @staticmethod
  def createShape(type):
    if type.lower() == 'square':
      return Square()
    elif type.lower() == 'rectangle':
      return Rectangle()
    elif type.lower() == 'circle':
      return Circle()
    else:
      return None