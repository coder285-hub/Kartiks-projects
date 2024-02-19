from validators import validate_email


def main():
    email = input("Please enter your email address: ")
    if validate_email(email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
