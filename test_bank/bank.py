def main():
    greeting_input = input("Greeting: ")
    print(f"${calculate_balance(greeting_input)}")

def calculate_balance(greeting):
    balances = {
        "hello": 0,
        "hi": 20,
    }

    total_balance = 0

    words = greeting.lower().strip().split()  # Split the greeting into words

    for word in words:
        if word[0].lower()=="hi": # Convert the word to lowercase before checking
            total_balance += 20  # Add the balance for "hi" to the total balance
        elif word[0].lower()=="hello":
            total_balance += 0  # Add the balance for "hello" to the total balance
        else:
            total_balance += 100  # Add the default balance to the total balance

    return total_balance

if __name__ == "__main__":
    main()
