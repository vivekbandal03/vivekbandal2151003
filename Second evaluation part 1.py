# Initialize an empty inventory dictionary
inventory = {}

def add_item(item_name, quantity, price):
    if item_name in inventory:
        print("Item already exists. Use the 'update' option to modify it.")
    else:
        inventory[item_name] = {'quantity': quantity, 'price': price}
        print(f"{item_name} added to inventory.")

def update_item(item_name, quantity, price):
    if item_name in inventory:
        inventory[item_name]['quantity'] = quantity
        inventory[item_name]['price'] = price
        print(f"{item_name} updated.")
    else:
        print(f"{item_name} does not exist in inventory.")

def remove_item(item_name):
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from inventory.")
    else:
        print(f"{item_name} does not exist in inventory.")

def generate_report():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for item_name, item_info in inventory.items():
            print(f"Item: {item_name}, Quantity: {item_info['quantity']}, Price: ${item_info['price']}")

while True:
    print("\nOptions:")
    print("1. Add item to inventory")
    print("2. Update item in inventory")
    print("3. Remove item from inventory")
    print("4. Generate inventory report")
    print("5. Exit")
    
    choice = input("Select an option (1/2/3/4/5): ")
    
    if choice == '1':
        item_name = input("Enter the item name: ")
        try:
            quantity = int(input("Enter the quantity: "))
            price = float(input("Enter the price: $"))
            add_item(item_name, quantity, price)
        except ValueError:
            print("Invalid input. Quantity and price should be numeric values.")
    elif choice == '2':
        item_name = input("Enter the item name: ")
        try:
            quantity = int(input("Enter the updated quantity: "))
            price = float(input("Enter the updated price: $"))
            update_item(item_name, quantity, price)
        except ValueError:
            print("Invalid input. Quantity and price should be numeric values.")
    elif choice == '3':
        item_name = input("Enter the item name to remove: ")
        remove_item(item_name)
    elif choice == '4':
        generate_report()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
