def planeTicket(hasRoom, hasPlaneTicket):
    if hasRoom and hasPlaneTicket:
        return " You will get the gold discount!"
    elif hasRoom or hasPlaneTicket:
        return " You will get the silver discount!"
    else:
        return " You are not eligible for a plane ticket"
    
print(planeTicket(False, True))