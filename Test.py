def planeTicket(hasRoom, hasPlaneTicket):
    if hasRoom and hasPlaneTicket:
        return " You will get the gold discount!"
    elif hasRoom or hasPlaneTicket:
        return " You will get the silver discount!"
    else:
        return " You are not eligible for a plane ticket"
    
print(planeTicket(False, True))

#Create a movie class. Your movie class should include 4 parameters.
#Then create 3 move objects from your class.

class movie:
    def __init__(self, title, director, genre, release_year):
        self.title = title
        self.director = director
        self.genre = genre
        self.release_year = release_year

movie1 = movie("Daredevil", "Mark Steven Johnson", "Action", 2003)
movie2 = movie("The Dark Knight", "Christopher Nolan", "Action", 2008)
movie3 = movie("Home", "Tim Johnson", "Animation", 2015)

#https://web.dragonball-api.com/