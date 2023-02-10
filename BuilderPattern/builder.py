class Car:
    def __init__(self, brand: str, model: str, color: str):
        self.brand = brand
        self.model = model
        self.color = color

class CarBuilder:
    def __init__(self):
        self.brand = ""
        self.model = ""
        self.color = "red"

    def set_brand(self, brand: str):
        self.brand = brand
        return self

    def set_model(self, model: str):
        self.model = model
        return self

    def set_color(self, color: str):
        self.color = color
        return self

    def build(self):
        return Car(
            brand=self.brand,
            model=self.model,
            color=self.color
        )

builder = CarBuilder().set_brand("Ford").set_model("Mustang").set_color("green")
print(builder.__dict__)
car = builder.build()
print(car.__dict__)
