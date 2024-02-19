from validators import validate_email, ValidationFailure


def main():
    email = input("Please enter your email address: ")
    try:
        if validate_email(email):
            print("Valid")
        else:
            print("Invalid")
    except ValidationFailure:
        print("Invalid")


if __name__ == "__main__":
    main()
