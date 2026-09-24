import rental_system as structural

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
# todo: do uzupełnienia

print("\n############################################")
print("SCENARIUSZ 2: brak sprzętu na stanie")
print("############################################")

print("--- Wersja strukturalna ---")
reset_structural()
structural.add_member("Ola", "ola@mail.com", is_premium=False)
structural.add_equipment("Kajak", 200, 0)
structural.rent_equipment("Ola", ["Kajak"])

print("--- Wersja OOP ---")
# todo: do uzupełnienia


print("\n############################################")
print("SCENARIUSZ 3: nieznany klient")
print("############################################")

print("--- Wersja strukturalna ---")
reset_structural()
structural.rent_equipment("Ktoś", ["Rower"])

print("--- Wersja OOP ---")
# todo: do uzupełnienia
