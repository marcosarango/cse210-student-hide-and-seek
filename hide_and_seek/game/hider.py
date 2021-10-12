from _typeshed import Self
import random

# TODO: Define the Hider class here
class Hider():
    def __init__(self):
        self.location = random.randint(1, 1000)
        self.distance = [0,0]

    def get_hint(self):
        message_hider = "(-.-) call me when you are close" 
        if self.distance[-1] == 0:
            message_hider = (f"(;.;) You found me")
        elif self.distance[-1] < self.distance[-2]:
            message_hider = (f"(^.^) Getting colder")
        elif self.distance[-1] > self.distance[-2]:
            message_hider = (f"(>.<) getting warner")
        
        return message_hider
    
    def watch(self, location):
        distance = abs(self.location - location)
        self.distance.append(distance)
       
    

