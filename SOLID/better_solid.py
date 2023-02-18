from abc import ABC, abstractmethod

class Motor(ABC):
    @abstractmethod
    def start(self):
        pass

class Verbrennungsmotor(Motor):
    def start(self):
        print("Verbrennungsmotor gestartet")

class Elektromotor(Motor):
    def start(self):
        print("Elektromotor gestartet")

class Auto:
    def __init__(self, motor: Motor):
        self.motor = motor
        self._speed = 0
        self._started = False

    def start(self):
        self.motor.start()
        print("Auto gestartet")
        self._started = True

    def beschleunigen(self, amount: int):
        if not self._started:
            raise ValueError("Das Auto wurde nicht gestartet")
        self._speed += amount

    def bremsen(self, amount: int):
        if not self._started:
            raise ValueError("Das Auto wurde nicht gestartet")
        self._speed -= amount
