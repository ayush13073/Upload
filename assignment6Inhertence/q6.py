class Device:
    def __init__(self, device_id, powered):
        self.device_id = device_id
        self.powered = powered

    def device_details(self):
        if self.powered:
            status = "ON"
        else:
            status = "OFF"
        print("Device ID = %d, Power = %s" % (self.device_id, status))


class Laptop(Device):
    def __init__(self, device_id, powered, ram):
        Device.__init__(self, device_id, powered)
        self.ram = ram

    def device_details(self):
        Device.device_details(self)
        print("Laptop RAM = %d GB" % self.ram)


class Mobile(Device):
    def __init__(self, device_id, powered, camera):
        Device.__init__(self, device_id, powered)
        self.camera = camera

    def device_details(self):
        Device.device_details(self)
        print("Mobile Camera = %d MP" % self.camera)


class SmartDevice(Laptop, Mobile):
    def __init__(self, device_id, powered, ram, camera):
        Laptop.__init__(self, device_id, powered, ram)
        self.camera = camera

    def device_details(self):
        Laptop.device_details(self)
        print("SmartDevice Camera = %d MP" % self.camera)


sd = SmartDevice(1, True, 16, 64)
sd.device_details()