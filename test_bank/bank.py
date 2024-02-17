def main():
    greeting_input = input("Greeting: ")
    result = value(greeting_input)
    print(result)

def value(greeting):
    balances = {
        "hello": 0,
        "hi": 20,
    }

    total_balance = 0

    words = greeting.lower().strip().split()  # Split the greeting into words

    for word in words:
        if word in balances:
            total_balance += balances[word]

    if total_balance > 0:
        return f"${total_balance}"
    else:
        return "$100"  # Default return if no valid words are found

if __name__ == "__main__":
    main()

