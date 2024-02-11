def main():
    # Define accepted denominations and price
    accepted_coins = [25, 10, 5]
    price = 50
    
    # Initialize variables
    amount_inserted = 0
    
    # Prompt the user to insert coins until the price is reached
    while amount_inserted < price:
        coin = int(input("Insert coin (25, 10, or 5 cents): "))
        
        # Check if the coin is an accepted denomination
        if coin in accepted_coins:
            amount_inserted += coin
            print("Amount due:", price - amount_inserted, "cents")
        else:
            print("Invalid coin. Accepted denominations are 25, 10, and 5 cents.")
    
    # Calculate and output the change owed
    change = amount_inserted - price
    print("Change owed:", change, "cents")

if __name__ == "__main__":
    main()

