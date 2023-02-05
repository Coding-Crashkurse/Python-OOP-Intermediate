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


class EngineFactory:
    @staticmethod
    def create_engine(engine_type: str):
        if engine_type == "verbrennungsmotor":
            return Verbrennungsmotor()
        elif engine_type == "elektromotor":
            return Elektromotor()
        else:
            raise ValueError(f"Motor typ nicht unterstützt: {engine_type}")


motor = EngineFactory.create_engine("verbrennungsmotor")
auto = Auto(motor)
auto.start()

motor = EngineFactory.create_engine("elektromotor")
auto = Auto(motor)
auto.start()
