def main():
    amount_due = 50
    while amount_due > 0:
        print("Amount Due:", amount_due)
        amount_due -= check_coins()
    print("Change Owed: ", abs(amount_due))

def check_coins():
    while True:
        coins = int(input("Insert Coin: "))
        if coins  == 25 or coins == 10 or coins == 5:
            break
    return coins

main()
