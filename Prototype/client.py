from prototypeRegistry import PrototypeRegistry
import time


print("making registry")
starttime = time.time()
registry = PrototypeRegistry()
print("done, total time: ", time.time() - starttime)

print("extracting the same product from registry")
starttime = time.time()
productOne1 = registry.getProduct("Product 1")
productOne2 = registry.getProduct("Product 1")
productOne3 = registry.getProduct("Product 1")
productOne4 = registry.getProduct("Product 1")
print("done, total time: ", time.time() - starttime)

print(id(productOne1), id(productOne2), id(productOne2))