class BankNewsletter:
    def __init__(self):
        self.customers = []

    def register(self, customer: "Customer"): # forward reference
        self.customers.append(customer)

    def unregister(self, customer: "Customer"):
        self.customers.remove(customer)

    def notify_customers(self, message: str):
        for customer in self.customers:
            customer.update(message)


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.newsletter = None

    def subscribe(self, newsletter: BankNewsletter):
        self.newsletter = newsletter
        self.newsletter.register(self)

    def unsubscribe(self):
        if not self.newsletter:
            raise ValueError("Kunde ist nicht subscribed.")
        self.newsletter.unregister(self)
        self.newsletter = None

    def update(self, message: str):
        print(f"{self.name} hat Nachricht erhalten: {message}")


Kunde1 = Customer("John")
Kunde2 = Customer("Jane")

newsletter = BankNewsletter()

Kunde1.subscribe(newsletter)
Kunde2.subscribe(newsletter)

newsletter.notify_customers("Neues Sparkonto mit hohem Zinssatz jetzt verfügbar!")

Kunde1.unsubscribe()
newsletter.notify_customers("Sonderrabatt auf alle Privatkredite!")
