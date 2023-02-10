class Motor:
    def start(self):
        print("start")


class Auto:
    def __init__(self, motor: Motor):
        self.motor = motor

    def start(self):
        self.motor.start()
        print("Auto gestartet")


class GPS:
    def __init__(self, auto: Auto):
        self.auto = auto

    def start(self):
        print("GPS aktiviert")
        self.auto.start()


motor = Motor()
auto = Auto(motor)
auto.start()

auto = GPS(auto)
auto = GPS(auto)
auto = GPS(auto)
auto = GPS(auto)

auto.start()
