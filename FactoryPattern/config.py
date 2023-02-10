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


import configparser
import os


class EngineFactory:
    @staticmethod
    def create_engine(engine_type: str):
        if engine_type == "verbrennungsmotor":
            return Verbrennungsmotor()
        elif engine_type == "elektromotor":
            return Elektromotor()
        else:
            raise ValueError(f"Motorentyp nicht supportet: {engine_type}")


config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), "FactoryPattern", "config.ini"))
engine_type = config.get("ENGINE", "type")
motor = EngineFactory.create_engine(engine_type)
auto = Auto(motor)
auto.start()
