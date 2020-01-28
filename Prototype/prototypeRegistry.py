from prototype import ProductOne, ProductTwo, ProductThree
import copy


class PrototypeRegistry:

  def __init__(self):
    self.prototypeMap = {}
    self.prototypeMap["Product 1"] = ProductOne()
    self.prototypeMap["Product 2"] = ProductTwo()
    self.prototypeMap["Product 3"] = ProductThree()

  
  def getProduct(self, name):
    return copy.copy(self.prototypeMap[name])