from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def construct(self):
        self.build_frame()
        self.install_engine()
        self.install_wheels()
        self.add_accessories()

    @abstractmethod
    def build_frame(self):
        pass

    @abstractmethod
    def install_engine(self):
        pass

    @abstractmethod
    def install_wheels(self):
        pass

    @abstractmethod
    def add_accessories(self):
        pass


class Car(Vehicle):
    def build_frame(self):
        print("Building car frame")

    def install_engine(self):
        print("Installing car engine")

    def install_wheels(self):
        print("Installing 4 wheels")

    def add_accessories(self):
        print("Adding car accessories")


class Motorcycle(Vehicle):
    def build_frame(self):
        print("Building motorcycle frame")

    def install_engine(self):
        print("Installing motorcycle engine")

    def install_wheels(self):
        print("Installing 2 wheels")

    def add_accessories(self):
        print("Adding motorcycle accessories")


car = Car()
car.construct()

motorcycle = Motorcycle()
motorcycle.construct()
