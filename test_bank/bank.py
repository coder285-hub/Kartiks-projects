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
            return 20  # Use the lowercase word as the key

        elif word[0].lower()=="hello":
            return 0
        else:
            return 100 # Default return if no valid words are found

if __name__ == "__main__":
    main()

