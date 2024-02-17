def main():
    greeting_input = input("Greeting: ")
    result = value(greeting_input)
    print(result)

def value(greeting):
    balances = {
        "hello": 0,
        "hi": 20,
    }

    greeting = greeting.lower().strip()

    greeting = greeting.lower().strip()

    if greeting in balances:  # Check if the whole greeting is in balances
        return f"${balances[greeting]}"  

if __name__ == "__main__":
    main()

