import seasons

def test_number_to_words():
    assert seasons.number_to_words(0) == "zero"
    assert seasons.number_to_words(9) == "nine"
    assert seasons.number_to_words(12) == "twelve"
    assert seasons.number_to_words(20) == "twenty"
    assert seasons.number_to_words(25) == "twenty-five"
    assert seasons.number_to_words(98) == "ninety-eight"
    assert seasons.number_to_words(100) == "greater than ninety-nine"

def test_calculate_age_in_minutes():
    # Test with a known birth date
    birth_date = seasons.parse_date("1990-01-01")
    # Leap years: 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020
    # Leap years from 1990 to 2023: 8
    # Non-leap years: 1991, 1993, ..., 2019, 2021, 2022, 2023
    # Non-leap years from 1990 to 2023: 34
    # Total minutes: 34 * 365 * 24 * 60 + 8 * 366 * 24 * 60 = 892,476,000
    assert seasons.calculate_age_in_minutes(birth_date) == 892476000

    # Test with a birth date on a leap year
    birth_date = seasons.parse_date("1992-02-29")
    # Leap years from 1992 to 2023: 8
    # Non-leap years from 1992 to 2023: 32
    # Total minutes: 32 * 365 * 24 * 60 + 9 * 366 * 24 * 60 = 915,984,000
    assert seasons.calculate_age_in_minutes(birth_date) == 915984000

def test_parse_date():
    assert seasons.parse_date("2000-01-01") == seasons.date(2000, 1, 1)
    assert seasons.parse_date("1999-12-31") == seasons.date(1999, 12, 31)
    assert seasons.parse_date("2024-02-19") == seasons.date(2024, 2, 19)

# Run the tests
test_number_to_words()
test_calculate_age_in_minutes()
test_parse_date()

