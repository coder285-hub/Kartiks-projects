def has_minimum_length(s):
    return len(s) >= 2

def has_maximum_length(s):
    return len(s) <= 6

def has_only_letters_and_numbers(s):
    return s.isalnum()

def has_valid_number_placement(s):
    if any(char.isdigit() for char in s):
        last_char = s[-1]
        if last_char.isdigit() and last_char != '0':
            return True
    return False

def is_valid(s):
    if has_minimum_length(s) and has_maximum_length(s) and \
            has_only_letters_and_numbers(s) and has_valid_number_placement(s):
        return True
    else:
        return False

def main():
    plate = input("Enter your vanity plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()

