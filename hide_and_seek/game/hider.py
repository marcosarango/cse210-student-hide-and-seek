
import random

# TODO: Define the Hider class here

class Hider():
    """the resposability for this class is to hind for the seeker.
    
    steriotype:
    Information Holder

    Attributes:
    location(int): the location of my hoder 1-100.
    distance(list): the distance of my seeker.
    """
    def __init__(self):
        """ Class constructor. Instance atributes
        
        argument:
          self(Hider): this is a instance of Hider

        """
        
        self.location = random.randint(1, 1000)
        self.distance = [0,0]

    def get_hint(self):
        """
        The hider give a hit fot the seeker

        argument:
           self(Hider): this a instance of Hider
        
           
        """
        message_hider = "(-.-) call me when you are close" 
        if self.distance[-1] == 0:
            message_hider = (f"(;.;) You found me")
        elif self.distance[-1] < self.distance[-2]:
            message_hider = (f"(^.^) Getting colder")
        elif self.distance[-1] > self.distance[-2]:
            message_hider = (f"(>.<) getting warner")
        
        return message_hider
    
    def watch(self, location):
        """
        This only watch the location and give distance
        """
        distance = abs(self.location - location)
        self.distance.append(distance)
       
    

