def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):

    if not plate[:2].isalpha():
        return False
    
    # Rule 2: Plate must have a minimum of 2 characters and a maximum of 6 characters
    if not 2 <= len(plate) <= 6:
        return False
    
    # Rule 3: The first number used cannot be '0'
    if plate[0].isdigit() and plate[0] == '0':
        return False
    
    # Rule 4: No periods, spaces, or punctuation marks are allowed
    if any(not c.isalnum() for c in plate):
        return False
    
    return True


main()
