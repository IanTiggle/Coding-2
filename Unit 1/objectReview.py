# 1. In your own words, describe what a class property is. Please write your response as a string.

"A class property is a variable that is associated with a class and it stores data for that specific class."

# 2. In your own words, describe what a class method is. Please write your response as a string.

"A class method is a function that is associated with a class and it performs a specific action for that class."

# 3. Create a student class. This function should create unique student objects. Your class needs to have 4 properties and 3 methods.
# Once you created the class, create 2 student objects. Each should be using a method from your class.

# 4. Create a video game character class funtion. This function should create unique video game character objects.
# Your class needs to have 4 properties and 3 methods. Once you created the class, create 2 video game character objects.
# Each should be using a method from your class.
 
class Student:
    def __init__(self, name, age, grade, studentID):
        self.name = name
        self.age = age
        self.grade = grade
        self.studentID = studentID

    def study(self):
        print(self.name + " is studying.")

    def skippingClass(self):
        print(self.name + " is skipping class.")

    def attendClass(self):
        print(self.name + " is attending class.")
    
student_1 = Student("Alice", 20, "A", "12345")
student_2 = Student("Bob", 22, "B", "67890")

student_1.study()
student_1.attendClass()

student_2.skippingClass()


class VideoGameCharacter:
    def __init__(self, name, health, strength, level):
        self.name = name
        self.health = health
        self.strength = strength
        self.level = level

    def attack(self):
        print(self.name + " is attacking.")

    def defend(self):
        print(self.name + " is defending.")

    def levelUp(self):
        self.level += 1
        print(self.name + " has leveled up to level " + str(self.level) + "!")

character_1 = VideoGameCharacter("Warrior", 100, 50, 1)
character_2 = VideoGameCharacter("Mage", 80, 70, 1)

character_1.defend()
character_1.attack()

character_2.attack()
character_2.levelUp()

