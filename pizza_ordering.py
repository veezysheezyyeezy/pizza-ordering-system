"""
Pizza Ordering System
A portfolio-style Python project that demonstrates list operations, sorting, and data handling.
"""


def main():
    """Run the pizza inventory and pricing demo."""
    toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
    prices = [2, 6, 1, 3, 2, 7, 2]

    print("=" * 55)
    print("🍕 PIZZA ORDERING SYSTEM 🍕")
    print("=" * 55)

    num_two_dollar_slices = prices.count(2)
    print(f"Number of $2 pizzas: {num_two_dollar_slices}")

    num_pizzas = len(toppings)
    print(f"Total pizza varieties: {num_pizzas}")
    print(f"We sell {num_pizzas} different kinds of pizza!")

    pizza_and_prices = [
        [2, "pepperoni"],
        [6, "pineapple"],
        [1, "cheese"],
        [3, "sausage"],
        [2, "olives"],
        [7, "anchovies"],
        [2, "mushrooms"],
    ]
    pizza_and_prices.sort()

    cheapest_pizza = pizza_and_prices[0]
    priciest_pizza = pizza_and_prices[-1]

    print(f"\nCheapest pizza: ${cheapest_pizza[0]:.2f} - {cheapest_pizza[1].title()}")
    print(f"Most expensive pizza: ${priciest_pizza[0]:.2f} - {priciest_pizza[1].title()}")

    pizza_and_prices.pop(-1)
    pizza_and_prices.insert(2, [2.5, "peppers"])

    three_cheapest = pizza_and_prices[:3]
    print("\nThree cheapest options:")
    for index, pizza in enumerate(three_cheapest, 1):
        print(f"  {index}. ${pizza[0]:.2f} - {pizza[1].title()}")

    print("\n" + "=" * 55)
    print("Available pizzas listed above.")
    print("=" * 55)


if __name__ == "__main__":
    main()
