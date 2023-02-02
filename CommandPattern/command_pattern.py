from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class VerbrennungsmotorStartCommand(Command):
    def execute(self):
        print("Verbrennungsmotor gestartet")


class ElektromotorStartCommand(Command):
    def execute(self):
        print("Elektromotor gestartet")


class Auto:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def start(self):
        self.command.execute()
        print("Auto gestartet")


auto = Auto()
auto.set_command(VerbrennungsmotorStartCommand())
auto.start()

auto.set_command(ElektromotorStartCommand())
auto.start()
