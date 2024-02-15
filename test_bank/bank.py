def main():
    greeting_input = input("Greeting: ")
    result = value(greeting_input)
    print(result)



def value(greeting):
    balances = {
        "hello": 0,
        "h": 20,
    }

    greeting = greeting.lower().strip()

    if greeting in balances:
        return f"${balances[greeting]}"
    else:
        return "$100"


if __name__ == "__main__":
    main()
