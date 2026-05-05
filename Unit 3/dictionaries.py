# A python dictionary is a collection type that stores values that describe unique data.
# IT IS A OBJECT!
# It's similar to a class object but with less rules.
# There are no methods on dictionaries

srProm = {
"name": "Senior Prom",
"date": "May 8th, 2026",
"gradeLevel" : "12th",
}

srFieldTrip = {
    "name": "Senior Field Trip",
    "date": "May 22nd, 2026",
    "gradeLevel" : "12th",
    "timeLeaving" : "6 AM",
    "timeReturning" : "12 AM"
}

graduation = {
    "name": "Graduation",
    "date": "June 2nd, 2026",
    "gradeLevel" : "12th",
}

#print(graduation["date"])
# Class is function that CREATES OBJECTS- these objects need to follow the class rules
# dictionaries are natual objects
class event():
    def __init__(self, name):
        self.name = name

events = [graduation, srFieldTrip, srProm]

#print(event)

for specialOccassion in events: 
    print(specialOccassion ["name"], "-", specialOccassion ["date"])