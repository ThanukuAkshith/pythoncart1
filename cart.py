from products import products

cart = []
max_items = 8

def view_products():
    print("\n===== Available Products =====")
    for p in products:
        print(f"ID: {p['id']} | {p['name']} | Price: ₹{p['price']} | Stock: {p['stock']}")
    print("="*30)

def add_to_cart(product_id, quantity):
    global cart


    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break

    if product is None:
        print("Invalid Product ID.")
        return

    if quantity > product["stock"]:
        print(f"Only {product['stock']} items available in stock.")
        return


    for item in cart:
        if item["id"] == product_id:
            item["quantity"] += quantity
            product["stock"] -= quantity
            print(f"Updated {product['name']} quantity to {item['quantity']}.")
            return

    if len(cart) >= max_items:
        print("Cart limit reached (max 8 items).")
        return

    cart.append({
        "id": product["id"],
        "name": product["name"],
        "price": product["price"],
        "quantity": quantity
    })
    product["stock"] -= quantity
    print(f"Added {product['name']} x{quantity} to cart.")

def view_cart():
    global cart
    if not cart:
        print("\nCart is empty.")
        return

    print("\n===== Your Cart =====")
    total = 0
    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        print(f"{item['name']} | ₹{item['price']} x {item['quantity']} = ₹{subtotal}")
    print(f"Total Amount: ₹{total}")
    print("="*30)

def update_cart(product_id, quantity):
    global cart
    for item in cart:
        if item["id"] == product_id:
            product = None
            for p in products:
                if p["id"] == product_id:
                    product = p
                    break
            if product is None:
                return

            change = quantity - item["quantity"]  
            if change > product["stock"]:
                print(f"Cannot update. Only {product['stock']} more items available.")
                return

            item["quantity"] = quantity
            product["stock"] -= change
            print(f"Updated {item['name']} to {quantity}.")
            return
    print("Product not found in cart.")

def remove_from_cart(product_id):
    global cart
    for item in cart:
        if item["id"] == product_id:
            product = None
            for p in products:
                if p["id"] == product_id:
                    product = p
                    break
            if product:
                product["stock"] += item["quantity"]

            cart.remove(item)
            print(f"Removed {item['name']} from cart.")
            return
    print("Product not found in cart.")

def checkout():
    global cart
    if not cart:
        print("Cart is empty, nothing to checkout.")
        return
    view_cart()
    print("Thank you for shopping with us!")
    cart.clear()
