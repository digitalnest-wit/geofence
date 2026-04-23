from .locations import Location
from math import sqrt

class Zone:
    def __init__(self, name:str, location:Location, radius:float):
        self.name = name 
        self.location = location 
        self.radius = radius 

    def contains(self, location:Location)-> bool:
        distance = sqrt(
            (self.location.x - location.x) ** 2 + 
            (self.location.y - location.y)
        )     
        return distance <= self.radius 