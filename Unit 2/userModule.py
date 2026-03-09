class car:
    def __init__(self, year, color, brand):
        self.year = year
        self.color = color
        self.brand = brand

    def unlock(self):
        print("The car has been unlocked.")
    
    def start_engine(self):
        print("The engine has started.")

car1 = car(2020, "Red", "Toyota")
print(car1.year)

car1.unlock()