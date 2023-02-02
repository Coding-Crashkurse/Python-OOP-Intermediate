from abc import ABC, abstractmethod


class StartStrategy(ABC):
    @abstractmethod
    def start(self):
        pass


class VerbrennungsmotorStart(StartStrategy):
    def start(self):
        print("Verbrennungsmotor gestartet")


class ElektromotorStart(StartStrategy):
    def start(self):
        print("Elektromotor gestartet")


class Auto:
    def __init__(self, start_strategy: StartStrategy):
        self.start_strategy = start_strategy

    def set_start_strategy(self, start_strategy: StartStrategy):
        self.start_strategy = start_strategy

    def start(self):
        self.start_strategy.start()
        print("Auto gestartet")


auto = Auto(VerbrennungsmotorStart())
auto.start()

auto.set_start_strategy(ElektromotorStart())
auto.start()
