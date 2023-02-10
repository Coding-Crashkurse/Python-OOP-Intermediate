class Car:
    _instance = None

    # def __new__(cls, *args, **kwargs):
    #     if not cls._instance:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            raise ValueError("A Car instance already exists.")
        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, brand: str, model: str, color: str):
        if not hasattr(self, "brand"):
            self.brand = brand
            self.model = model
            self.color = color


car1 = Car(brand="Opel", model="Corsa", color="red")
car2 = Car(brand="Opelsda", model="Cosrsa", color="red")

print(car1.__dict__)
