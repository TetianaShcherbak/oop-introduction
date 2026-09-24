class Equipment:
    def __init__(self, name, deposit, quantity):
        self.name = name
        self.deposit = deposit
        self.quantity = quantity

    def is_available(self):
        return self.quantity > 0

    def reserve(self):
        if not self.is_available():
            raise ValueError(f"Brak '{self.name}' na stanie")
        self.quantity -= 1

