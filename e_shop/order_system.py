customers = []
products = []
orders = []

def add_customer(name, email, is_vip):
    customers.append({"name": name, "email": email, "is_vip": is_vip})

def add_product(name, price, stock):
    products.append({"name": name, "price": price, "stock": stock})

def calculate_discount(customer, total):
    if customer["is_vip"]:
        return total * 0.15
    elif total > 200:
        return total * 0.05
    return 0

def create_order(customer_name, product_names):
    customer = None
    for c in customers:
        if c["name"] == customer_name:
            customer = c
    if customer is None:
        print("Brak klienta")
        return

    total = 0
    items = []
    for pname in product_names:
        for p in products:
            if p["name"] == pname:
                if p["stock"] <= 0:
                    print(f"Brak {pname} na magazynie")
                    return
                total += p["price"]
                p["stock"] -= 1
                items.append(pname)

    discount = calculate_discount(customer, total)
    final_price = total - discount

    orders.append({
        "customer": customer_name,
        "items": items,
        "total": total,
        "discount": discount,
        "final_price": final_price
    })
    print(f"Zamówienie dla {customer_name}: {final_price} zł (rabat: {discount} zł)")

def print_order_summary(customer_name):
    for o in orders:
        if o["customer"] == customer_name:
            print(f"{o['customer']}: {o['items']} -> {o['final_price']} zł")


# --- przykład użycia ---
if __name__ == "__main__":
    add_customer("Anna", "anna@mail.com", is_vip=True)
    add_customer("Tomek", "tomek@mail.com", is_vip=False)

    add_product("Laptop", 3000, 5)
    add_product("Myszka", 50, 10)
    add_product("Klawiatura", 120, 8)

    create_order("Anna", ["Laptop", "Myszka"])
    create_order("Tomek", ["Myszka", "Klawiatura"])

    print_order_summary("Anna")
    print_order_summary("Tomek")