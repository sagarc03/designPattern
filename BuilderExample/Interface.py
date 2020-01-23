import abc

class VehicleInterface(abc.ABC):
  @abc.abstractmethod
  def setBody(self, body):
    raise NotImplementedError

  @abc.abstractmethod
  def setEngine(self, engine):
    raise NotImplementedError

  @abc.abstractmethod
  def setColor(self, color):
    raise NotImplementedError

  @abc.abstractmethod
  def setNoOfPeople(self, noOfPeople):
    raise NotImplementedError

  @abc.abstractmethod
  def setCargo(self, cargo):
    raise NotImplementedError

  
class Builder(abc.ABC):

  @abc.abstractmethod
  def buildBody(self):
    raise NotImplementedError

  @abc.abstractmethod
  def buildEngine(self):
    raise NotImplementedError

  @abc.abstractmethod
  def buildColor(self):
    raise NotImplementedError

  @abc.abstractmethod
  def buildNoOfPeople(self):
    raise NotImplementedError

  @abc.abstractmethod
  def buildCargo(self):
    raise NotImplementedError

  @abc.abstractmethod
  def getVehicle(self):
    raise NotImplementedError