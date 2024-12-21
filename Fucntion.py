def display_menu():
    """Display the menu with food items and their prices."""
    menu = {
        "Burger": 5.99,
        "Pizza": 8.99,
        "Pasta": 7.49,
        "Salad": 4.99,
        "Coffee": 1.49
    }
    
    print("Welcome to the Simple Food Ordering System!")
    print("Here is the menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    
    return menu

def get_order(menu):
    """Prompt the user to select an item from the menu."""
    while True:
        order = input("\nPlease select an item from the menu (enter the name exactly as listed): ")
        if order in menu:
            return order, menu[order]
        else:
            print("Invalid item. Please select an item from the menu.")

def process_payment(total_cost):
    """Process the payment and ensure the amount is sufficient."""
    while True:
        try:
            cash = float(input(f"\nThe total cost is ${total_cost:.2f}. Please enter cash amount: $"))
            if cash >= total_cost:
                change = cash - total_cost
                print(f"Payment accepted. Your change is ${change:.2f}.")
                break
            else:
                print("Insufficient funds. Please provide more cash.")
        except ValueError:
            print("Invalid input. Please enter a valid cash amount.")

def main():
    """Main function to run the food ordering system."""
    menu = display_menu()
    order, price = get_order(menu)
    print(f"\nYou have selected {order} which costs ${price:.2f}.")
    
    total_cost = price
    process_payment(total_cost)

if __name__ == "__main__":
    main()
