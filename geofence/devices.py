from .locations import Location

class Device:
    def __init__(self, id:str, location:Location):
        self.id = id
        self.current_location = location
    
    def update_location(self, location:Location):
        ...