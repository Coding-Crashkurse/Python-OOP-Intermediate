# Schlechter Code


class Motor:
    def start(self):
        print("Motor gestartet")


class Auto:
    def __init__(self):
        self.motor = Motor()

    def start(self):
        self.motor.start()
        print("Auto gestartet")


auto = Auto()
auto.start()


# Guter Code
class Motor:
    def start(self):
        print("Motor started")


class Auto:
    def __init__(self, motor):
        self.motor = motor

    def start(self):
        self.motor.start()
        print("Auto started")


motor = Motor()
auto = Auto(motor)
auto.start()

from abc import ABC, abstractmethod


class BaseEngine(ABC):
    @abstractmethod
    def start(self):
        pass


class Verbrennungsmotor(BaseEngine):
    def start(self):
        print("Verbrennungsmotor gestartet")


class Elektromotor(BaseEngine):
    def start(self):
        print("Elektromotor gestartet")


class Auto:
    def __init__(self, motor: BaseEngine):
        self.motor = motor

    def start(self):
        self.motor.start()
        print("Auto gestartet")


motor = Verbrennungsmotor()
auto = Auto(motor)
auto.start()

motor = Elektromotor()
auto = Auto(motor)
auto.start()
