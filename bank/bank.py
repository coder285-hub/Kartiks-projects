balances ={"Hello":0,"Hello, Newman":0,"How you doing":20,"What's happening?":100}

user_input=input()

if user_input in balances:
    print("$"+balances[user_input])
else:
    print("Invalid Input")
