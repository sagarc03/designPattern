class MechanicalEngineer:
  
  def __init__(self, vehicleBuilder):
    self.vehicleBuilder = vehicleBuilder
  
  def make(self):
    self.vehicleBuilder.buildBody()
    self.vehicleBuilder.buildEngine()
    self.vehicleBuilder.buildColor()
    self.vehicleBuilder.buildNoOfPeople()
    self.vehicleBuilder.buildCargo()
  
  def get(self):
    return self.vehicleBuilder.getVehicle()