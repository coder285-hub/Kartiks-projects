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

    for letter in greeting:

        if letter in balances:
            return f"${balances[greeting]}

    return "$100"


if __name__ == "__main__":
    main()
