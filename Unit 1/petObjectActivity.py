class Pets:
    def __init__(self, name, species, age, color, weight):
        self.name = name
        self.species = species
        self.age = age
        self.color = color
        self.weight = weight
        
        def eat(self):
            print(self.name + " is eating")
        
        def sleep(self):
            print(self.name + " is sleeping")

        def play(self):
            print(self.name + " is playing")

        def home_wrecker(self, food):
            if food == 0:
                print(self.name + " is being a home wrecker")
            else:
                print(self.name + " is not being a home wrecker")

pet1 = Pets("Cloud", "Cat", 2, "White", 10)
pet2 = Pets("Princess", "Dog", 5, "Brown", 30)
pet3 = Pets("Snoopy", "Dog", 8, "White and Black", 15)


pet1.home_wrecker(0)
    