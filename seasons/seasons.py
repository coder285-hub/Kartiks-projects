from datetime import date, datetime
import sys

def calculate_age_in_minutes(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    total_minutes = age * 365 * 24 * 60  # non-leap years
    leap_years = sum(1 for year in range(birth_date.year, today.year + 1) if is_leap_year(year))
    total_minutes += leap_years * 24 * 60  # additional minutes for leap years
    return total_minutes

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")
        sys.exit(1)

def main():
    birth_date_str = input("Enter your date of birth (YYYY-MM-DD): ")
    birth_date = parse_date(birth_date_str)
    age_in_minutes = calculate_age_in_minutes(birth_date)
    print("You are {} minutes old.".format(number_to_words(round(age_in_minutes))))

def number_to_words(num):
    # Define words for numbers up to 20
    numbers_up_to_20 = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    # Define words for tens
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if num < 20:
        return numbers_up_to_20[num]
    elif num < 100:
        return tens[num // 10] + ('' if num % 10 == 0 else '-' + numbers_up_to_20[num % 10])
    else:
        return "greater than ninety-nine"

if __name__ == "__main__":
    main()
