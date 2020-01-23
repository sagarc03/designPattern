import Interface
import Vehicle

class CarBuilder(Interface.Builder):

  def __init__(self):
    self.car = Vehicle.Vehicle()

  def buildBody(self):
    self.car.setBody('sedan')

  def buildEngine(self):
    self.car.setEngine('car engine')

  def buildColor(self):
    self.car.setColor('blue')

  def buildNoOfPeople(self):
    self.car.setNoOfPeople(5)

  def buildCargo(self):
    self.car.setCargo('trunk')

  def getVehicle(self):
    return self.car


class TruckBuilder(Interface.Builder):

  def __init__(self):
    self.truck = Vehicle.Vehicle()

  def buildBody(self):
    self.truck.setBody('truk')

  def buildEngine(self):
    self.truck.setEngine('truck engine')

  def buildColor(self):
    self.truck.setColor('black')

  def buildNoOfPeople(self):
    self.truck.setNoOfPeople(3)

  def buildCargo(self):
    self.truck.setCargo('Large')

  def getVehicle(self):
    return self.truck
    

class BikeBuilder(Interface.Builder):

  def __init__(self):
    self.bike = Vehicle.Vehicle()

  def buildBody(self):
    self.bike.setBody('Bike')

  def buildEngine(self):
    self.bike.setEngine('Bike engine')

  def buildColor(self):
    self.bike.setColor('red')

  def buildNoOfPeople(self):
    self.bike.setNoOfPeople(2)

  def buildCargo(self):
    self.bike.setCargo('None')

  def getVehicle(self):
    return self.bike