def main():
    greeting_input = input("Greeting: ")
    result = calculate_balance(greeting_input)  # Use the correct function name
    print(result)

def calculate_balance(greeting):
    balances = {
        "hello": 0,
        "hi": 20,
    }

    total_balance = 0

    words = greeting.lower().strip().split()  # Split the greeting into words

    for word in words:
        if word.lower() in balances:  # Convert the word to lowercase before checking
            total_balance += balances[word.lower()]  # Use the lowercase word as the key

    if total_balance > 0:
        return f"${total_balance}"
    else:
        return "$100"  # Default return if no valid words are found

if __name__ == "__main__":
    main()

