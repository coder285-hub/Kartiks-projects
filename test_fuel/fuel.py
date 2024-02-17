def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        result = gauge(percentage)
        print(result)
    except (ValueError, ZeroDivisionError) as e:
        print(e)


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if not (isinstance(x, int) and isinstance(y, int)):
        raise ValueError("Both X and Y must be integers.")
    if x > y:
        raise ValueError("X cannot be greater than Y.")
    if y == 0:
        raise ZeroDivisionError("Denominator (Y) cannot be zero.")
    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
