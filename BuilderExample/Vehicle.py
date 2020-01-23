import Interface

class Vehicle(Interface.VehicleInterface):
  _body = None
  _engine = None
  _color = None
  _noOfPeople = None
  _cargo = None

  def setBody(self, body):
    self._body = body

  def setEngine(self, engine):
    self._engine = engine

  def setColor(self, color):
    self._color = color

  def setNoOfPeople(self, noOfPeople):
    self._noOfPeople = noOfPeople

  def setCargo(self, cargo):
    self._cargo = cargo

  def __str__(self):
    return "{} {} {} {} {}".format(
                              self._body,
                              self._color,
                              self._engine,
                              self._noOfPeople,
                              self._cargo
                              )



