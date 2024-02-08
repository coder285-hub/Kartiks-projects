def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    amount_str = amount_str.lstrip('$')
    # Convert the string to a float
    return float(amount_str)


def percent_to_float(p):
    percentage_str = percentage_str.rstrip('%')
    # Convert the string to a float and divide by 100 to get the decimal representation of the percentage
    return float(percentage_str) / 100


main()
