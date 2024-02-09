balances ={"Hello":0,"Hello, Newman":0,"How you doing":20,"What's happening?":100}

user_input=input("Greeting: ")

if user_input in balances:
    print("$"+str(balances[user_input]))
    
else:
    print("Invalid Input")
