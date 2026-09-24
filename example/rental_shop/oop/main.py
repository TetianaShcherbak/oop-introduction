from rental_shop import RentalShop
from member import Member
from equipment import Equipment

if __name__ == "__main__":
    shop = RentalShop()

    shop.add_member(Member("Marek", "marek@mail.com", is_premium=True))
    shop.add_member(Member("Ola", "ola@mail.com", is_premium=False))
    shop.add_member(Member("Kasia", "kasia@mail.com", is_student=True))
    shop.add_member(Member("Olek", "olek@mail.com", is_student=True))


    shop.add_equipment(Equipment("Rower", 100, 5))
    shop.add_equipment(Equipment("Kajak", 200, 2))

    rental_marek = shop.rent_equipment("Marek", ["Rower", "Kajak"])
    rental_ola = shop.rent_equipment("Ola", ["Rower"])
    rental_kasia = shop.rent_equipment("Kasia", ["Rower"])
    rental_olek = shop.rent_equipment("Olek", ["Rower", "Kajak"])


    print("\n--- Opłaty karne za 3 dni spóźnienia ---")
    print(f"Marek (premium): {rental_marek.calculate_late_fee(3)} zł")
    print(f"Ola (regular): {rental_ola.calculate_late_fee(3)} zł")
    print(f"Kasia (student, 1 przedmiot): {rental_kasia.calculate_late_fee(3)} zł")
    print(f"Olek (student, 2 przedmioty): {rental_olek.calculate_late_fee(3)} zł")

