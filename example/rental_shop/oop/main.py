from rental_shop import RentalShop
from member import Member
from equipment import Equipment

if __name__ == "__main__":
    shop = RentalShop()

    shop.add_member(Member("Marek", "marek@mail.com", is_premium=True))
    shop.add_member(Member("Ola", "ola@mail.com", is_premium=False))

    shop.add_equipment(Equipment("Rower", 100, 3))
    shop.add_equipment(Equipment("Kajak", 200, 2))

    shop.rent_equipment("Marek", ["Rower", "Kajak"])
    shop.rent_equipment("Ola", ["Rower"])
