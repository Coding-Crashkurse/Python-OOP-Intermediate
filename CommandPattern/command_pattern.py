class Car:
    def __init__(self):
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        print(f"Accelerating, new speed is {self.speed}")

    def brake(self, amount):
        self.speed -= amount
        print(f"Braking, new speed is {self.speed}")


class Command:
    def execute(self):
        pass


class AccelerateCommand(Command):
    def __init__(self, car, amount):
        self.car = car
        self.amount = amount

    def execute(self):
        self.car.accelerate(self.amount)


class BrakeCommand(Command):
    def __init__(self, car, amount):
        self.car = car
        self.amount = amount

    def execute(self):
        self.car.brake(self.amount)


class Remote:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()
        self.commands.clear()


car = Car()
remote = Remote()

accelerate_command = AccelerateCommand(car, 10)
brake_command = BrakeCommand(car, 5)

remote.add_command(accelerate_command)
remote.add_command(accelerate_command)
remote.add_command(accelerate_command)
remote.add_command(brake_command)

remote.execute_commands()
