from Director import MechanicalEngineer
from Builder import CarBuilder, TruckBuilder, BikeBuilder


enggineer1 = MechanicalEngineer(CarBuilder())
enggineer2 = MechanicalEngineer(BikeBuilder())
enggineer3 = MechanicalEngineer(TruckBuilder())

enggineer1.make()
print(enggineer1.get())
enggineer2.make()
print(enggineer2.get())
enggineer3.make()
print(enggineer3.get())
