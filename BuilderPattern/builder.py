class Engine:
    def __init__(self, horsepower: int, num_cylinders: int):
        self.horsepower = horsepower
        self.num_cylinders = num_cylinders

    def __str__(self):
        return f"Engine with {self.horsepower} horsepower and {self.num_cylinders} cylinders."

class Car:
    def __init__(self, make: str, model: str, engine: Engine):
        self.make = make
        self.model = model
        self.engine = engine

    def __str__(self):
        return f"{self.make} {self.model} with {self.engine}"

class CarBuilder:
    def __init__(self):
        self.make = ""
        self.model = ""
        self.horsepower = 0
        self.num_cylinders = 0

    def set_make(self, make: str):
        self.make = make
        return self

    def set_model(self, model: str):
        self.model = model
        return self

    def set_horsepower(self, horsepower: int):
        self.horsepower = horsepower
        return self

    def set_num_cylinders(self, num_cylinders: int):
        self.num_cylinders = num_cylinders
        return self

    def build(self):
        return Car(
            make=self.make,
            model=self.model,
            engine=Engine(
                horsepower=self.horsepower,
                num_cylinders=self.num_cylinders
            )
        )

builder = CarBuilder().set_make("Ford").set_model("Mustang").set_horsepower(400).set_num_cylinders(8)
car = builder.build()
print(car)
# Output: Ford Mustang with Engine with 400 horsepower and 8 cylinders.
