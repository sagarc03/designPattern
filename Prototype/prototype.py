from interface import ProductInterface
from ExternalAPI import API

class ProductOne(ProductInterface):

  def __init__(self):
    self.name = API.getName("Product 1")

  def getName(self):
    return self.name


class ProductTwo(ProductInterface):

  def __init__(self):
    self.name = API.getName("Product 2")

  def getName(self):
    return self.name


class ProductThree(ProductInterface):

  def __init__(self):
    self.name = API.getName("Product 3")

  def getName(self):
    return self.name

