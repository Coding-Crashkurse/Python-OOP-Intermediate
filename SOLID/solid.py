class Auto:
    def __init__(self, motor_type: str):
        self.motor_type = motor_type
        self._speed = 0
        self._started = False

    def start(self):
        if self.motor_type == "Verbrennungsmotor":
            print("Verbrennungsmotor gestartet")
        elif self.motor_type == "Elektromotor":
            print("Elektromotor gestartet")
        else:
            raise ValueError("Unbekannter Motortyp")
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
