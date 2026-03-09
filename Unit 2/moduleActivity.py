# 1. In your own words, what is a Phython module / library?
# Please write your answer as a string

"A python module is a file that contains code that you can quickly access with having to type the code again."

# 2. Inside your unit folder, create a new document called userModule.py. Then, create a class that creates a car model class.
# Your class should have 3 properties and 2 methods.

# 3. In this document (moduleActivity) import your car class and create car objects.
# Print out the name and brand of the car and use 1 method on each car.

import userModule

car1 = userModule.car(2020, "Red", "Toyota")
car2 = userModule.car(2021, "Blue", "Honda")

print(car1.year)
print(car1.brand)
car1.unlock()

