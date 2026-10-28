"""
Question 6: Hybrid Inheritance.
Base class: Device with method device_details(DeviceID, Powered)
Derived class: Laptop with method laptop_details
Derived class: Mobile with method mobile_details
Derived class: SmartPhone(Laptop, Mobile) with method smartphone_details

Note: The question in the document was cut off after "Laptop", so this
program uses Laptop and Mobile as the two branches and SmartPhone as the
combined class to demonstrate hybrid inheritance.
"""


class Device:
    def device_details(self, device_id, powered):
        print("Device ID:", device_id, "Powered:", powered)


class Laptop(Device):
    def laptop_details(self, ram):
        print("Laptop RAM:", ram)


class Mobile(Device):
    def mobile_details(self, camera):
        print("Mobile camera:", camera)


class SmartPhone(Laptop, Mobile):
    def smartphone_details(self, model):
        print("SmartPhone model:", model)


phone = SmartPhone()
phone.device_details(101, True)
phone.laptop_details("8GB")
phone.mobile_details("48MP")
phone.smartphone_details("Galaxy")
