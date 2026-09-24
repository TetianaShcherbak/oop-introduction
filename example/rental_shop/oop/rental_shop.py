from member import Member
from equipment import Equipment
from rental import Rental

class RentalShop:
    def __init__(self):
        self.members = {}
        self.equipment = {}
        self.rentals = []

    def add_member(self, member: Member):
        self.members[member.name] = member

    def add_equipment(self, item: Equipment):
        self.equipment[item.name] = item

    def rent_equipment(self, member_name, equipment_names):
        member = self.members.get(member_name)
        if member is None:
            print("Brak członka")
            return None

        rental = Rental(member)
        try:
            for ename in equipment_names:
                item = self.equipment.get(ename)
                if item is None:
                    print(f"Nieznany sprzęt: {ename}")
                    return None
                rental.add_equipment(item)
        except ValueError as e:
            print(e)
            return None

        self.rentals.append(rental)
        print(rental.summary())
        return rental

