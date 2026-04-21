from .locations import Location


class Zone:
    def __init__(self, name:str, location:Location, radius:float):
        self.name = name 
        self.location = location 
        self.radius = radius 

        def contains(self, location:Location)-> bool:
            ...







  

    

