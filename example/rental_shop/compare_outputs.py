import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "oop"))

import rental_system as structural
from rental_shop import RentalShop
from member import Member
from equipment import Equipment


def reset_structural():
    """Czyścimy globalny stan modułu przed każdym scenariuszem."""
    structural.members.clear()
    structural.equipment.clear()
    structural.rentals.clear()

print("############################################")
print("SCENARIUSZ 1: podstawowe wypożyczenie")
print("############################################")

print("--- Wersja strukturalna ---")
reset_structural()
structural.add_member("Marek", "marek@mail.com", is_premium=True)
structural.add_equipment("Rower", 100, 3)
structural.rent_equipment("Marek", ["Rower"])

print("--- Wersja OOP ---")
shop = RentalShop()
shop.add_member(Member("Marek", "marek@mail.com", is_premium=True))
shop.add_equipment(Equipment("Rower", 100, 3))
shop.rent_equipment("Marek", ["Rower"])


print("\n############################################")
print("SCENARIUSZ 2: brak sprzętu na stanie")
print("############################################")

print("--- Wersja strukturalna ---")
reset_structural()
structural.add_member("Ola", "ola@mail.com", is_premium=False)
structural.add_equipment("Kajak", 200, 0)
structural.rent_equipment("Ola", ["Kajak"])

print("--- Wersja OOP ---")
shop = RentalShop()
shop.add_member(Member("Ola", "ola@mail.com", is_premium=False))
shop.add_equipment(Equipment("Kajak", 200, 0))
shop.rent_equipment("Ola", ["Kajak"])

print("\n############################################")
print("SCENARIUSZ 3: nieznany klient")
print("############################################")

print("--- Wersja strukturalna ---")
reset_structural()
structural.rent_equipment("Ktoś", ["Rower"])

print("--- Wersja OOP ---")
shop = RentalShop()
shop.rent_equipment("Ktoś", ["Rower"])
