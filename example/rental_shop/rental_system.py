members = []
equipment = []
rentals = []

def add_member(name, email, is_premium):
    members.append({"name": name, "email": email, "is_premium": is_premium})

def add_equipment(name, deposit, quantity):
    equipment.append({"name": name, "deposit": deposit, "quantity": quantity})

def calculate_late_fee(member, days_late):
    if member["is_premium"]:
        return days_late * 2
    return days_late * 5

def rent_equipment(member_name, equipment_names):
    member = None
    for m in members:
        if m["name"] == member_name:
            member = m
    if member is None:
        print("Brak członka")
        return

    total_deposit = 0
    items = []
    for ename in equipment_names:
        for e in equipment:
            if e["name"] == ename:
                if e["quantity"] <= 0:
                    print(f"Brak {ename} na stanie")
                    return
                total_deposit += e["deposit"]
                e["quantity"] -= 1
                items.append(ename)

    rentals.append({
        "member": member_name,
        "items": items,
        "total_deposit": total_deposit
    })
    print(f"Wypożyczenie dla {member_name}: kaucja {total_deposit} zł")


if __name__ == "__main__":
    add_member("Marek", "marek@mail.com", is_premium=True)
    add_member("Ola", "ola@mail.com", is_premium=False)

    add_equipment("Rower", 100, 3)
    add_equipment("Kajak", 200, 2)

    rent_equipment("Marek", ["Rower", "Kajak"])
    rent_equipment("Ola", ["Rower"])
