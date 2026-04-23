from .locations import Location
from .devices import Device
from .zones import Zone
from .alerts import Alert

class System:
    def __init__(self, system:str):
        self.system = system 
        self.__zone_registry:list[Zone] = []
        self.__device_registry:list[Device]=[]
        self.__location_registry:list[Location]=[]
        self.__alerts:list[Alert]=[]

    @property
    def zone_registry(self):
        return self.__zone_registry
    
    @property
    def device_registry(self):
        return self.__device_registry
    
    @property 
    def location_registry(self):
        return self.__location_registry
    
    @property 
    def alerts(self):
        return self.__alerts
    
    def register_device(self, device: Device):
        self.__device_registry.append(device)

    
    def register_zone(self, zone: Zone):
        self.__zone_registry.append(zone)


    def update_device_location(self,location: Location):
        ...

    def alert_logs(self ):
        ...

