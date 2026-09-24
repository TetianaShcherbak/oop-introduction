from member import Member
from equipment import Equipment

class Rental:
    def __init__(self, member: Member):
        self.member = member
        self.items = []
        self.total_deposit = 0

    def add_equipment(self, item: Equipment):
        item.reserve()
        self.items.append(item)
        self.total_deposit += item.deposit

    def summary(self):
        item_names = [i.name for i in self.items]
        return (f"Wypożyczenie dla {self.member.name}: {item_names} -> "
                f"kaucja {self.total_deposit:.2f} zł")

