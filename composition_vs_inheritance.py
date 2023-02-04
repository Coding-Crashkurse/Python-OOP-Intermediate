class Motor:
    def start(self):
        print("Motor gestartet")

class Auto:
    def __init__(self):
        self.engine = Motor()

    def start(self):
        print("Auto gestartet")
        self.engine.start()

class Motor:
    def start(self):
        print("Motor gestartet")

class Auto(Motor):
    def start(self):
        print("Auto gestartet")
        super().start()
