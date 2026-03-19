# In your unit 3 folder, create a new document called activityMar19.py Copy and paste the questions into your document and then
#  answer the following questions. You are permitted to use your notes, w3schools, and work together to answer the questions.
# do your best to complete all questions. This activity is due at the end of class.


# 1. In your own words, what is the difference between a python class and a python object?
# Please write your resonse as a string data type. 
"The difference between a python class and a python object is that a class is a template for creating objects,"
" while an object is the result of you using the template of a class."
" A class defines the properties and methods that an object will have,"
" while an object is an instance of a class"
" that has its own unique values for those properties and can use the methods defined in the class."

# 2. In your own words, what is a object property and and object method? Please
# write your response as a string data type.
"The difference between an object property and an object method is that a property is a variable that belongs to an object,"
" while a method is a function that belongs to an object."

# 3. Create a unique python class. Your class should have 5 properties and 3 mtethods. 
# each method should do one of the following; 
# 1 method must do some type of operation with data; an arithmetic, logical, or comparison operation
# 1 method must take in a parameter and do some operation on the parameter
# 1 method must do some type of conditional (if/else) logic. 

class pythonClass:
    def __init__(self, folder, name, type, size, color):
        self.folder = folder
        self.name = name
        self.type = type
        self.size = size
        self.color = color

    def operation(self):
        return self.size * 2
    
    def parameter(self, new_size):
        self.size = new_size
        return self.size
    
    def conditional(self):
        if self.type == "text":
            return "This is a text file."
        elif self.type == "image":
            return "This is an image file."
        else:
            return "This is a different type of file."
        