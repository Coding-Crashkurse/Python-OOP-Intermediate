class Beverage:
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def brew(self):
        pass

    def pour_in_cup(self):
        print("Pouring into cup")

    def add_condiments(self):
        pass

class Tea(Beverage):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding Lemon")

class Coffee(Beverage):
    def brew(self):
        print("Dripping Coffee through filter")

    def add_condiments(self):
        print("Adding Sugar and Milk")

tea = Tea()
tea.prepare()

coffee = Coffee()
coffee.prepare()
