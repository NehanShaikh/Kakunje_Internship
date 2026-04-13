# Task5
from abc import ABC, abstractmethod

class Mobile(ABC):
    def __init__(self, pin):
        self.__pin = pin

    def verify_pin(self, entered):
        if entered == self.__pin:
            print("PIN Verified")
        else:
            print("Incorrect PIN")

    def change_pin(self, old, new):
        if old == self.__pin:
            self.__pin = new
            print("PIN Changed Successfully")
        else:
            print("Wrong Old PIN")

    @abstractmethod
    def device_info(self):
        pass

class SmartPhone(Mobile):
    def device_info(self):
        print("SmartPhone Device")

phone = SmartPhone(1234)
phone.verify_pin(1234)
phone.change_pin(1234, 5678)
