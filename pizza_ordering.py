#!/usr/bin/env python3
"""Pizza Shop Ordering System

A polished beginner-friendly Python project for a portfolio.
Users can browse a menu, add pizzas, customize toppings,
view their receipt, and calculate the total with tax.
"""

from typing import List, Dict, Tuple

PIZZA_MENU = [
    {"id": 1, "name": "Margherita", "base_price": 12.50, "description": "Tomato sauce, mozzarella, basil"},
    {"id": 2, "name": "Pepperoni Feast", "base_price": 14.75, "description": "Pepperoni, tomato sauce, mozzarella"},
    {"id": 3, "name": "Veggie Supreme", "base_price": 15.25, "description": "Olives, mushrooms, peppers, onions"},
    {"id": 4, "name": "BBQ Chicken", "base_price": 16.50, "description": "BBQ sauce, chicken, red onion, cheese"},
    {"id": 5, "name": "Hawaiian", "base_price": 14.25, "description": "Ham, pineapple, mozzarella"},
]

EXTRA_TOPPINGS = {
    1: ("Pepperoni", 2.50),
    2: ("Mushrooms", 1.75),
    3: ("Olives", 1.50),
    4: ("Pineapple", 1.75),
    5: ("Onions", 1.25),
    6: ("Extra Cheese", 2.00),
    7: ("Peppers", 1.50),
}


def display_banner() -> None:
    """Print the application title and header."""
    print("\n" + "=" * 60)
    print("        🍕 WELCOME TO SUNSET PIZZA CO. 🍕")
    print("=" * 60)


def display_menu() -> None:
    """Show all available pizzas."""
    print("\nAvailable Pizzas:\n")
    for pizza in PIZZA_MENU:
        print(
            f"  {pizza['id']}. {pizza['name']} - ${pizza['base_price']:.2f}"
            f" | {pizza['description']}"
        )

    print("\nOptional Extra Toppings:")
    for topping_id, (name, price) in EXTRA_TOPPINGS.items():
        print(f"  {topping_id}. {name} - ${price:.2f}")


def get_pizza_by_id(pizza_id: str):
    """Return a pizza dictionary by its ID."""
    for pizza in PIZZA_MENU:
        if str(pizza["id"]) == pizza_id:
            return pizza
    return None


def get_topping_by_id(topping_id: str):
    """Return the topping name and price by topping ID."""
    topping = EXTRA_TOPPINGS.get(int(topping_id))
    if topping is None:
        return None
    return topping


def add_pizza_to_order() -> Dict:
    """Prompt the user to choose a pizza and optional extras."""
    display_menu()

    pizza_choice = input("\nChoose a pizza by number: ").strip()
    pizza = get_pizza_by_id(pizza_choice)

    if pizza is None:
        print("That pizza number is not valid. Please try again.")
        return add_pizza_to_order()

    chosen_toppings = []
    while True:
        add_more = input("Add a topping? (y/n): ").strip().lower()

        if add_more == "n":
            break
        if add_more != "y":
            print("Please enter 'y' or 'n'.")
            continue

        topping_choice = input("Choose a topping number: ").strip()
        topping = get_topping_by_id(topping_choice)

        if topping is None:
            print("That topping is not available. Please try again.")
            continue

        topping_name, topping_price = topping
        chosen_toppings.append({"name": topping_name, "price": topping_price})
        print(f"Added {topping_name} for ${topping_price:.2f}.")

    order_item = {
        "pizza": pizza,
        "toppings": chosen_toppings,
    }
    return order_item


def calculate_total(order: List[Dict]) -> Tuple[float, float, float]:
    """Calculate subtotal, tax, and total for the order."""
    subtotal = 0.0

    for item in order:
        subtotal += item["pizza"]["base_price"]
        for topping in item["toppings"]:
            subtotal += topping["price"]

    tax_rate = 0.085
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    return subtotal, tax_amount, total


def print_receipt(customer_name: str, order: List[Dict]) -> None:
    """Display the final receipt for the customer."""
    print("\n" + "~" * 60)
    print(f"Customer: {customer_name}")
    print("Order Summary:\n")

    for index, item in enumerate(order, start=1):
        pizza = item["pizza"]
        print(f"{index}. {pizza['name']} - ${pizza['base_price']:.2f}")

        if item["toppings"]:
            print("   Extras:")
            for topping in item["toppings"]:
                print(f"      - {topping['name']} - ${topping['price']:.2f}")

    subtotal, tax_amount, total = calculate_total(order)
    print("\n" + "-" * 60)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (8.5%): ${tax_amount:.2f}")
    print(f"Total: ${total:.2f}")
    print("\nThank you for ordering from Sunset Pizza Co!")
    print("~" * 60)


def main() -> None:
    """Run the pizza ordering application."""
    display_banner()
    customer_name = input("What's your name? ").strip() or "Guest"

    order = []
    while True:
        order.append(add_pizza_to_order())
        another = input("\nWould you like to add another pizza? (y/n): ").strip().lower()
        if another != "y":
            break

    print_receipt(customer_name, order)


if __name__ == "__main__":
    main()
