def main():
    user_input=input("Greeting: ")



def value(greeting):
    balances ={"Hello":0," Hello ":0,"Hello, Newman":0,"How you doing?":20,"What's happening?":100,"What's up?":100}


    if greeting in balances:
        return str(balances[greeting])

    else:
        print("Invalid Input")



if __name__ == "__main__":
    main()
