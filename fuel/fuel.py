def get_fraction():
    while True:
        try:
            fraction = input("Enter the fuel fraction (X/Y): ")
            x, y = map(int, fraction.split('/'))
            if x <= 0 or y <= 0 or x > y:
                raise ValueError("Invalid fraction")
            return x, y
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction (X/Y).")

def calculate_percentage(x, y):
    percentage = (x / y) * 100
    return round(percentage)

def main():
    while True:
        try:
            x, y = get_fraction()
            percentage = calculate_percentage(x, y)
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%)
            break
        except ZeroDivisionError:
            print("Denominator cannot be zero.")
        except ValueError as E:
            print(E)

if __name__ == "__main__":
    main()
