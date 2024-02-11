def convert(time_str):
    

def main():
    time = input("Enter the time in 24-hour format (e.g., 7:00): ")
    hour = convert(time)

    if 7.0 <= hour <= 8.0:
        print("It's breakfast time!")
    elif 12.0 <= hour <= 13.0:
        print("It's lunch time!")
    elif 18.0 <= hour <= 19.0:
        print("It's dinner time!")

if __name__ == "__main__":
    main()
