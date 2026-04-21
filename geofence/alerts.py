from datetime import datetime, timezone
from .devices import Device
from .zones import Zone


class Alert:
    def __init__(self, device: Device, zone: Zone, alert_type:str):
        self.device = device
        self.zone = zone
        self.date_time = datetime.now(timezone.utc).strftime("%H:%M %m/%d/%Y")
        self.alert_type = alert_type

    def notify(self):
        pass
