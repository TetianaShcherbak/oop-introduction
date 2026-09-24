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

    
    def calculate_late_fee(self, days_late):
        if self.member.is_student and len(self.items) <= 1:
            return days_late * 3
        elif self.member.is_premium:
            return days_late * 2
        return days_late * 5