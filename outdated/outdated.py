
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def get_iso_date():
    while True:
        user_input = input("Enter a date (in format MM/DD/YYYY or Month Day, Year): ").strip()
        parts = user_input.split("/")
        if len(parts) == 3:
            try:
                month = int(parts[0])
                day = int(parts[1])
                year = int(parts[2])
                if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
                    iso_date = f"{year:04d}-{month:02d}-{day:02d}"
                    return iso_date
                else:
                    print("Invalid date. Please enter a valid date.")
            except ValueError:
                print("Invalid input. Please enter a valid date.")
        else:
            parts = user_input.split(", ")
            if len(parts) == 3:
                try:
                    month = months.index(parts[0]) + 1
                    day = int(parts[1])
                    year = int(parts[2])
                    if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
                        iso_date = f"{year:04d}-{month:02d}-{day:02d}"
                        return iso_date
                    else:
                        print("Invalid date. Please enter a valid date.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid date.")
            else:
                print("Invalid input. Please enter a valid date.")

if __name__ == "__main__":
    iso_date = get_iso_date()
    print("ISO 8601 Date:", iso_date)
