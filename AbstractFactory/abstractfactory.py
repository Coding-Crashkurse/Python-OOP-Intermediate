from abc import ABC, abstractmethod


class BaseMotor(ABC):
    @abstractmethod
    def start(self):
        pass


class Verbrennungsmotor(BaseMotor):
    def start(self):
        print("Verbrennungsmotor gestartet")


class ElektroMotor(BaseMotor):
    def start(self):
        print("Elektromotor gestartet")


class Auto:
    def __init__(self, motor: BaseMotor):
        self.motor = motor

    def start(self):
        print("Auto wurde gestartet")
        self.motor.start()


class EngineFactory(ABC):
    @abstractmethod
    def create_engine(self):
        pass


class VerbrennungsmotorEngineFactory(EngineFactory):
    def create_engine(self):
        return Verbrennungsmotor()


class ElektromotorEngineFactory(EngineFactory):
    def create_engine(self):
        return ElektroMotor()


engine_factory = ElektromotorEngineFactory()
motor = engine_factory.create_engine()
auto = Auto(motor)
auto.start()

engine_factory = VerbrennungsmotorEngineFactory()
motor = engine_factory.create_engine()
auto = Auto(motor)
auto.start()
