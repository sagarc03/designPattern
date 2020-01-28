import abc

class ProductInterface(abc.ABC):

  @abc.abstractmethod
  def getName(self):
    pass