# Python OOP - Object Oriented Programming

# Object - a representation of some complex data structure.
# *data = data types (... and functions in this case)
# Although they maybe the smae thing, objectively, objects can different characteristics/ features.
# Class - is a constructor/ blueprint for creating objects.

# Properties - the data type values of a object.

class Computers:
    def __init__(self, name, color, shape, storage, portability, camera, ram, processor):
        self.name = name
        self.color = color
        self.shape = shape
        self.storage = storage
        self.portability = portability
        self.camera = camera
        self.ram = ram
        self.processor = processor

        def bluetoothConnection(self):
            print("")

        def internetConnectivity(self):
            print("")
        
        def powerOn(self):
            print("")
        
        def calculator(self):
            print("")

        def camera(self):
            print("")

        


class Phones:
    def __init__(self, storage, size, carrier, color, camera, name, warranty, price, brand):
        self.storage = storage
        self.size = size
        self.carrier = carrier
        self.color = color
        self.camera = camera
        self.name = name
        self.warranty = warranty
        self.price = price
        self.brand = brand

phone1 = Phones(16, "att", 13.00, "yellow", False, "brick Pro", False, 100.00, "brick")
phone2 = Phones(16, "verizon", 7.00, "blue", False, "brick mini", False, 100.00, "brick")


apple_1 = Computers("apple m4", "black", 10.00, 320, True, True, 120, "m4")
apple_2 = Computers("apple m5", "white", 10.00, 320, True, True, 80, "m5")


print(apple_1.ram)
print(apple_2.ram)