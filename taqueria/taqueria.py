menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def display_total_cost(order):
    total_cost = sum(menu[item] for item in order)
    return f"${total_cost:.2f}"

def main():
    order = []
    try:
        while True:
            item = input("Enter an item: ").strip().title()
            if item in menu:
                order.append(item)
                print("Total cost:", display_total_cost(order))
    except EOFError:
        pass

if __name__ == "__main__":
    main()
