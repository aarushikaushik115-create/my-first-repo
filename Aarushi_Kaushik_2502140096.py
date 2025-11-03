# ===============================================================
# Inventory Management System - Stationery Shop
# ---------------------------------------------------------------
# Name: Aarushi
# Enrolment No.: 2502140096
# ===============================================================

# --------------------- GLOBAL VARIABLES -------------------------
password = "aarushi"

inventory = {
    'pen': {'qty': 50, 'price': 10},
    'notebook': {'qty': 20, 'price': 40},
    'eraser': {'qty': 15, 'price': 5}
}

LOW_STOCK_THRESHOLD = 10

# --------------------- HELPER FUNCTIONS --------------------------
def pause():
    input("\nPress Enter to continue...")




# --------------------- CORE FUNCTIONS ----------------------------

def display_menu():
    print("1. Add New Item")
    print("2. View Inventory")
    print("3. Purchase (Add Stock)")
    print("4. Sell Item")
    print("5. Check Low Stock Items")
    print("6. Calculate Total Stock Value")
    print("7. Search for an Item")
    print("8. Update Item Price")
    print("9. Delete an Item")
    print("10. Exit")


# 1. Add New Item
def add_item():
    name = input("Enter item name: ").strip().lower()
    if name in inventory:
        print("Item already exists. Use Purchase to add stock.")
        return

    qty_input = input("Enter quantity: ").strip()
    price_input = input("Enter price (₹): ").strip()

    if qty_input.isdigit() and price_input.replace('.', '', 1).isdigit():
        qty = int(qty_input)
        price = float(price_input)
        inventory[name] = {'qty': qty, 'price': price}
        print(f"Item '{name}' added successfully.")
    else:
        print("Invalid input. Quantity and Price must be numeric.")

# 2. View Inventory
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("\nCurrent Inventory:")

    print(f"{'Item':15} {'Qty':>6} {'Price(₹)':>10}")

    for item, data in inventory.items():
        print(f"{item:15} {data['qty']:>6} {data['price']:>10.2f}")


# 3. Purchase Stock
def purchase_item():
    name = input("Enter item name to purchase: ").strip().lower()
    if name not in inventory:
        print("Item not found.")
        return

    qty_input = input("Enter quantity to add: ").strip()
    if qty_input.isdigit():
        qty = int(qty_input)
        inventory[name]['qty'] += qty
        print(f"Added {qty} units to '{name}'.")
    else:
        print("Invalid quantity entered.")

# 4. Sell Item
def sell_item():
    name = input("Enter item name to sell: ").strip().lower()
    if name not in inventory:
        print("Item not found.")
        return

    qty_input = input("Enter quantity to sell: ").strip()
    if qty_input.isdigit():
        n = int(qty_input)
        if inventory[name]['qty'] >= n:
            inventory[name]['qty'] -= n
            amount = inventory[name]['price'] * n
            print(f"Sale ₹{amount:.2f} | {name} qty={inventory[name]['qty']}")
            calculate_stock_value(show=False)
        else:
            print(f"Not enough stock. Only {inventory[name]['qty']} available.")
    else:
        print("Invalid quantity entered.")

# 5. Check Low Stock
def check_low_stock():
    print("\nLow Stock Items (Qty < Threshold):")

    found = False
    for item, data in inventory.items():
        if data['qty'] < LOW_STOCK_THRESHOLD:
            print(f"{item:15} -> Qty: {data['qty']}")
            found = True
    if not found:
        print("All items are sufficiently stocked.")


# 6. Calculate Stock Value
def calculate_stock_value(show=True):
    total = 0
    for data in inventory.values():
        total += data['qty'] * data['price']
    if show:
        print(f"Total Stock Value = ₹{total:.2f}")
    return total

# 7. Search Item
def search_item():
    name = input("Enter item name to search: ").strip().lower()
    if name in inventory:
        data = inventory[name]
        print(f"{name.capitalize()} -> Qty: {data['qty']}, Price: ₹{data['price']}")
    else:
        print("Item not found.")

# 8. Update Price
def update_price():
    name = input("Enter item name to update price: ").strip().lower()
    if name not in inventory:
        print("Item not found.")
        return

    price_input = input("Enter new price (₹): ").strip()
    if price_input.replace('.', '', 1).isdigit():
        new_price = float(price_input)
        inventory[name]['price'] = new_price
        print(f"Price of '{name}' updated to ₹{new_price:.2f}")
    else:
        print("Invalid price entered.")

# 9. Delete Item
def delete_item():
    name = input("Enter item name to delete: ").strip().lower()
    if name in inventory:
        del inventory[name]
        print(f"'{name}' deleted from inventory.")
    else:
        print("Item not found.")

# --------------------- MAIN LOOP --------------------------------
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_item()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            purchase_item()
        elif choice == '4':
            sell_item()
        elif choice == '5':
            check_low_stock()
        elif choice == '6':
            calculate_stock_value()
        elif choice == '7':
            search_item()
        elif choice == '8':
            update_price()
        elif choice == '9':
            delete_item()
        elif choice == '10':
            print("\nThank you for using the Stationery Shop Inventory System!")
            break
        else:
            print("Invalid choice. Please try again.")

        pause()

# --------------------- RUN PROGRAM ------------------------------
if __name__ == "__main__":
    print('============================================================')
    print("Welcome to the Stationery Shop Inventory Management System")
    print('============================================================')

    # Password Protection
    while True:
        user_password = input("Please enter password to proceed: ").strip()
        if user_password == password:
            print("Access Granted!\n")
            main()
            print("\nSession ended. Logging out...")
            print('============================================================')
            break
        else:
            print("Wrong password! Please try again.\n")
