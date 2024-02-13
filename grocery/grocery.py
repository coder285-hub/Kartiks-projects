def main():
    print("Enter the items you need from the grocery store (press Ctrl+D when finished):")
    groceries = {}
    try:
        while True:
            item = input().strip().lower()
            if item:
                if item in groceries:
                    groceries[item] += 1
                else:
                    groceries[item] = 1
    except EOFError:
        pass

    # Output the grocery list
    print("\nYour grocery list:")
    for item, count in sorted(groceries.items()):
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()

